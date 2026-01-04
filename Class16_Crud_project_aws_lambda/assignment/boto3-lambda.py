import boto3

lambda_client = boto3.client('lambda')
final_results = []

##### Function to print all lambda functions (name, runtime, and arn) #####

def print_lambda_functions():
    response = lambda_client.list_functions()
    functions = response.get('Functions', [])
    functions.sort(key=lambda f: f.get('FunctionName', ''))
    for function in functions:
        function_name = function.get('FunctionName')
        runtime = function.get('Runtime')
        arn = function.get('FunctionArn')
        print(f"Lambda Name   : {function_name}")
        print(f"Lambda Runtime: {runtime}")
        print(f"ARN           : {arn}")
        print("----")

# print("---- Listing Lambda Function Details ----")
# print("")
# print_lambda_functions()


##### Function to print all lambda functions along with their tags (name, version, tags) #####

def print_lambda_functions_and_tags():
    lambda_info = []
    paginator = lambda_client.get_paginator('list_functions')
    for page in paginator.paginate():
        functions = page.get('Functions', [])
        functions.sort(key=lambda f: f.get('FunctionName', ''))
        for fn in functions:
            name = fn.get('FunctionName')
            runtime = fn.get('Runtime')
            arn = fn.get('FunctionArn')
            try:
                tags_resp = lambda_client.list_tags(Resource=arn)
                tags = tags_resp.get('Tags', {}) or {}
            except Exception:
                tags = {}
            print(f"Lambda Name   : {name}")
            print(f"Lambda Runtime: {runtime}")
            if tags:
                print("Tags:")
                for k, v in tags.items():
                    print(f"  {k}: {v}")
            else:
                print("Tags: None")
            print("----")
            lambda_info.append({"name": name, "runtime": runtime, "arn": arn, "tags": tags})


# print("---- Listing Lambda Functions & Tags ----")
# print("")
# print_lambda_functions_and_tags()


##### Function to get specific tag value for a given lambda function #####

def get_lambda_tag_value(lambda_arn, tag_key):
    response = lambda_client.list_tags(Resource=lambda_arn)
    try:
      output = response.get('Tags')[tag_key]
    except KeyError:
    #   print(f"Tag key '{tag_key}' not found.")
      output = None

    return output


# print("---- Getting Specific Tag Value ----")
# print("")

# lambda_arn = 'arn:aws:lambda:us-east-1:307946636515:function:lambda_1'
# tag_key = 'owner'

# print(get_lambda_tag_value(lambda_arn, tag_key))


##### Function to return all lambda details as list of tuples #####

def get_all_lambda_function_details():
    response = lambda_client.list_functions()
    lambda_list = []
    functions = response.get('Functions', [])
    functions.sort(key=lambda f: f.get('FunctionName', ''))
    for function in functions:
        function_name = function['FunctionName']
        runtime = function['Runtime']
        lambda_arn = function['FunctionArn']
        lambda_list.append((function_name, runtime, lambda_arn))
    return lambda_list

# print("---- Getting All Lambda Function Details ----")
# print("")
# print(get_all_lambda_function_details())


##### Generate report of lambda name, python version and owner tag value #####

def generate_lambda_report():
    lambda_list = get_all_lambda_function_details()
    # print(lambda_list)
    for items in lambda_list:
        # print(items)
        name, version, arn = items
        # print(name, version, arn)
        owner = get_lambda_tag_value(arn, 'owner')
        print(f"Lambda Name: {name}, Lambda Version: {version}, owner: {owner}")

print("")
print("---- Generating Lambda Report ----")
print("")
generate_lambda_report()


##### Function to update python runtime for all lambdas with specific tag key/value #####

def update_python_runtime(target_runtime, tag_key, tag_value, dry_run=False):
    """
    Update all Lambda functions with tag_key=tag_value to the given target_runtime.
    This version does not use a paginator; it handles pages manually using the
    Marker/NextMarker pattern so beginners can follow the flow easily.

    Returns a list of tuples: (function_name, old_runtime, new_runtime_or_reason).
    """

    results = []
    marker = None

    while True:
        # Call list_functions, passing Marker when we have one to get the next page
        if marker:
            response = lambda_client.list_functions(Marker=marker)
        else:
            response = lambda_client.list_functions()
        
        # print("List Functions Response:")
        # print(type(response))
        # print(len(response))
        # print(len(response.get('Functions', [])))
        #print(response)

        functions = response.get('Functions', []) or []
        functions.sort(key=lambda f: f.get('FunctionName', ''))

        for fn in functions:
            name = fn.get('FunctionName')
            arn = fn.get('FunctionArn')
            runtime = fn.get('Runtime')

            # Get tags for this function (safe with try/except)
            try:
                tags = lambda_client.list_tags(Resource=arn).get('Tags') or {}
            except Exception:
                tags = {}

            # Check the tag match
            if tags.get(tag_key) != tag_value:
                continue

            # If runtime already matches
            if runtime == target_runtime:
                results.append((name, runtime, f"already_{target_runtime}"))
                continue

            # Dry-run prints what would be done
            if dry_run:
                print(f"[dry-run] Would update {name}: {runtime} -> {target_runtime}")
                results.append((name, runtime, "dry-run"))
                continue

            # Attempt the update
            try:
                resp = lambda_client.update_function_configuration(
                    FunctionName=name,
                    Runtime=target_runtime
                )
                new_runtime = resp.get('Runtime', target_runtime)
                print(f"Updated {name}: {runtime} -> {new_runtime}")
                results.append((name, runtime, new_runtime))
            except Exception as e:
                print(f"Failed to update {name}: {e}")
                results.append((name, runtime, f"error: {e}"))

        # Check for next page marker; if none, we're done
        marker = response.get('NextMarker')
        if not marker:
            break

    return results

print("")
print("---- Updating Python Runtime for Tagged Lambdas ----")
print("")

target_runtime, tag_key, tag_value = "python3.13", "owner", "cloud"

final_results = update_python_runtime(target_runtime, tag_key, tag_value, dry_run=False)

print("")
print("Updated Results:")
print("")

for res in final_results:
    name, old_runtime, new_runtime  = res
    print(f"Lambda Name: {name}, Old Runtime: {old_runtime}, New Runtime/Status: {new_runtime}, {tag_key}: {tag_value}")
    # print(res)


