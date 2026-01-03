#Simple print statements and data types
name = "Hemant"
place = "Pune"
print(f"Hello This is {name} from {place}")
print ("data-type of name is: ", type(name), "\ndata-type of place is: ", type(place))
print("-----------------------------")

#List and nested list
list1 = ["apple", "banana", "cherry", ["dog", "cat", "rat", [1,2,3,4]]]
print("list items:", list1)
print("nested item:", list1[3][1])
print("nested-nested item:", list1[3][3][3])
print("-----------------------------")

#Dictionary
dict1 = {
    "name": "Hemant",
    "city": "Pune",
    "skills": ["Python", "Aws", "Devops"],
    "education": {
        "undergrad": "B.Sc",
        "postgrad": "M.S"
    }
}   
print("Dictionary items:", dict1)
print("Name from dict:", dict1["name"]) 
print("Name from dict:", dict1.get("name")) 
print("Namee from dict:", dict1.get("namee")) 
print("Nameee from dict:", dict1.get("nameee", "Not Found" )) 
print("Undergrad degree:", dict1["education"]["undergrad"]) 
print("Postgrad degree:", dict1.get("education").get("postgrad")) 
print("Postgrade degree:", dict1.get("education").get("postgrade")) 
print("-----------------------------")

#tuple
tuple1 = ("red", "green", "blue", ("cyan", "magenta", "yellow"))
print("Tuple items:", tuple1)
print("Nested tuple item:", tuple1[3])
print("Nested-nested tuple item:", tuple1[3][1])
first,second,third,forth = tuple1
print("Unpacked values:", first, second, third, forth)
print("-----------------------------")

#Conditional statements
num1 = 10
num2 = 20
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}") 

if "Python" in dict1["skills"]:
    print("Python skill is present in dictionary")    
else:
    print("Python skill is not present in dictionary")

if isinstance(dict1, dict):
    print("dict1 is a dictionary")
else:
    print("dict1 is not a dictionary")

if isinstance(list1, list):
    print("list1 is a list")    
else:
    print("list1 is not a list")

if isinstance(place, list):
    print("place is a list")    
else:
    print("place is not a list")
print("-----------------------------")

#loops
print("Looping through list1:") 
for item in list1:
    print(item)
print("-----------------------------")
print("Looping through dict1:") 
for key in dict1:
    print(f"{key}: {dict1[key]}")   
print("-----------------------------")
#while loop
count = 0   
while count < 3:
    print("count is:", count)
    count += 1  
print("-----------------------------")
for i in range(3):
    print("i is:", i)   
print("-----------------------------")
for i in range(2, 5):
    print("i is:", i)
print("-----------------------------")
for i in range(0, 10, 3):
    print("i is:", i)
print("-----------------------------")
for key, value in dict1.items():
    print(f"{key}: {value}")    
print("-----------------------------")
print(dict1.keys())
print("-----------------------------")
print(dict1.values())
print("-----------------------------")
print(dict1.items())    
print("-----------------------------")
for item in dict1.items():
    print(item) 
print("-----------------------------")
for item in dict1.items():
    print("key of dictionary is:", item[0], " and value is:", item[1]) 
print("-----------------------------")
for key,value in dict1.items():
    print(f"key is {key} and value is {value}")
print("-----------------------------")

#Functions
def greet_user(username, greeting="Hello"):
    """Function to greet a user with a given greeting."""
    print(f"{greeting}, {username}!")

greet_user("Hemant")
greet_user("Sachin", "Welcome")
print("-----------------------------")

#add function
def add_numbers(a, b):
    """Function to add two numbers and return the result."""
    return a + b    

result = add_numbers(5, 10)
print("Sum is:", result)
print("-----------------------------")