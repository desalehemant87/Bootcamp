"""
Lab 5: Requests Module for HTTP Calls
======================================
Objective: Make HTTP requests and interact with APIs

Topics Covered:
- GET requests
- POST requests
- Request headers and parameters
- Response handling (status codes, headers, JSON)
- Error handling with requests
- Timeouts
- Working with REST APIs

Note: Run 'pip install requests' if not already installed
"""

import requests
import json
from datetime import datetime

# ========================================
# Exercise 1: Basic GET Requests
# ========================================
print("=" * 50)
print("Exercise 1: Basic GET Requests")
print("=" * 50)

# TODO: Simple GET request
print("Making GET request to JSONPlaceholder API:")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(f"Status Code: {response.status_code}")
print(f"Status: {'Success' if response.status_code == 200 else 'Failed'}")
print(f"\nResponse Headers:")
print(f"  Content-Type: {response.headers.get('content-type')}")
print(f"  Content-Length: {response.headers.get('content-length')}")

# TODO: Parse JSON response
if response.status_code == 200:
    data = response.json()
    print(f"\nResponse Data:")
    print(f"  Title: {data['title']}")
    print(f"  Body: {data['body'][:50]}...")

print()

# ========================================
# Exercise 2: GET Requests with Parameters
# ========================================
print("=" * 50)
print("Exercise 2: GET with Query Parameters")
print("=" * 50)

# TODO: Add query parameters
params = {
    'userId': 1,
    '_limit': 5
}

print(f"Requesting posts with parameters: {params}")
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

if response.status_code == 200:
    posts = response.json()
    print(f"\nReceived {len(posts)} posts:")
    for post in posts:
        print(f"  [{post['id']}] {post['title']}")

print()

# ========================================
# Exercise 3: POST Requests
# ========================================
print("=" * 50)
print("Exercise 3: POST Requests")
print("=" * 50)

# TODO: Create new resource with POST
new_post = {
    'title': 'DevOps with Python',
    'body': 'Learning to make HTTP requests with Python requests module',
    'userId': 1
}

print(f"Creating new post:")
print(f"  Title: {new_post['title']}")

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

if response.status_code == 201:
    created_post = response.json()
    print(f"\nPost created successfully!")
    print(f"  ID: {created_post['id']}")
    print(f"  Title: {created_post['title']}")
else:
    print(f"Failed to create post: {response.status_code}")

print()

# ========================================
# Exercise 4: Custom Headers
# ========================================
print("=" * 50)
print("Exercise 4: Custom Headers")
print("=" * 50)

# TODO: Send request with custom headers
headers = {
    'User-Agent': 'Python-DevOps-Bootcamp/1.0',
    'Accept': 'application/json',
    'X-Custom-Header': 'DevOps-Training'
}

print("Sending request with custom headers:")
for key, value in headers.items():
    print(f"  {key}: {value}")

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

if response.status_code == 200:
    data = response.json()
    print("\nHeaders received by server:")
    for key, value in data['headers'].items():
        print(f"  {key}: {value}")

print()

# ========================================
# Exercise 5: Status Code Handling
# ========================================
print("=" * 50)
print("Exercise 5: HTTP Status Code Handling")
print("=" * 50)

# TODO: Test different status codes
test_urls = [
    ("https://jsonplaceholder.typicode.com/posts/1", "Valid URL"),
    ("https://jsonplaceholder.typicode.com/posts/999999", "Non-existent resource"),
    ("https://httpbin.org/status/404", "404 Not Found"),
    ("https://httpbin.org/status/500", "500 Server Error"),
]

print("Testing different status codes:")
for url, description in test_urls:
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

        if status == 200:
            print(f"  {description}: SUCCESS (200)")
        elif status == 404:
            print(f"  {description}: NOT FOUND (404)")
        elif status >= 500:
            print(f"  {description}: SERVER ERROR ({status})")
        else:
            print(f"  {description}: STATUS {status}")

    except requests.RequestException as e:
        print(f"  {description}: ERROR - {e}")

print()

# ========================================
# Exercise 6: Timeout Handling
# ========================================
print("=" * 50)
print("Exercise 6: Timeout Handling")
print("=" * 50)

# TODO: Request with timeout
print("Making request with 5-second timeout:")
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )
    print(f"Request completed in time: {response.status_code}")
except requests.Timeout:
    print("Request timed out!")
except requests.RequestException as e:
    print(f"Request failed: {e}")

# TODO: Simulate timeout (httpbin delay)
print("\nTesting with delayed response (3 second delay, 5 second timeout):")
try:
    response = requests.get(
        "https://httpbin.org/delay/3",
        timeout=5
    )
    print(f"Request completed: {response.status_code}")
except requests.Timeout:
    print("Request timed out!")

print()

# ========================================
# Exercise 7: Error Handling
# ========================================
print("=" * 50)
print("Exercise 7: Comprehensive Error Handling")
print("=" * 50)

def make_safe_request(url, method='GET', **kwargs):
    """Make a request with comprehensive error handling"""
    try:
        if method.upper() == 'GET':
            response = requests.get(url, timeout=10, **kwargs)
        elif method.upper() == 'POST':
            response = requests.post(url, timeout=10, **kwargs)
        else:
            return None, f"Unsupported method: {method}"

        # Check if request was successful
        response.raise_for_status()
        return response, None

    except requests.ConnectionError:
        return None, "Connection error - Unable to reach server"
    except requests.Timeout:
        return None, "Request timed out"
    except requests.HTTPError as e:
        return None, f"HTTP error: {e}"
    except requests.RequestException as e:
        return None, f"Request failed: {e}"

# Test the function
print("Testing safe request function:")
test_cases = [
    ("https://jsonplaceholder.typicode.com/posts/1", "Valid URL"),
    ("https://httpbin.org/status/404", "404 Error"),
    ("https://this-domain-does-not-exist-12345.com", "Connection Error"),
]

for url, description in test_cases:
    print(f"\n{description}:")
    response, error = make_safe_request(url)
    if error:
        print(f"  Error: {error}")
    else:
        print(f"  Success: Status {response.status_code}")

print()

# ========================================
# Exercise 8: Working with JSON APIs
# ========================================
print("=" * 50)
print("Exercise 8: Working with REST APIs")
print("=" * 50)

# TODO: GitHub API example
print("Fetching Python repository info from GitHub:")
try:
    response = requests.get(
        "https://api.github.com/repos/python/cpython",
        timeout=10
    )

    if response.status_code == 200:
        repo = response.json()
        print(f"\nRepository: {repo['full_name']}")
        print(f"  Description: {repo['description']}")
        print(f"  Stars: {repo['stargazers_count']:,}")
        print(f"  Forks: {repo['forks_count']:,}")
        print(f"  Language: {repo['language']}")
        print(f"  Open Issues: {repo['open_issues_count']}")
    else:
        print(f"Failed to fetch repository: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching repository: {e}")

print()

# ========================================
# Exercise 9: Real DevOps Scenario - Health Checks
# ========================================
print("=" * 50)
print("Exercise 9: Service Health Checks")
print("=" * 50)

def check_service_health(name, url, timeout=5):
    """Check if a service is healthy"""
    try:
        start_time = datetime.now()
        response = requests.get(url, timeout=timeout)
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        return {
            'name': name,
            'status': 'UP' if response.status_code == 200 else 'DOWN',
            'status_code': response.status_code,
            'response_time': f"{response_time:.2f}s",
            'error': None
        }
    except requests.RequestException as e:
        return {
            'name': name,
            'status': 'DOWN',
            'status_code': None,
            'response_time': None,
            'error': str(e)
        }

# Check multiple services
services = [
    ("JSONPlaceholder API", "https://jsonplaceholder.typicode.com/posts/1"),
    ("HTTPBin", "https://httpbin.org/status/200"),
    ("GitHub API", "https://api.github.com"),
]

print("Checking service health:")
results = []
for name, url in services:
    result = check_service_health(name, url)
    results.append(result)

    status_icon = "✓" if result['status'] == 'UP' else "✗"
    print(f"\n  {status_icon} {result['name']}: {result['status']}")
    if result['status_code']:
        print(f"    Status Code: {result['status_code']}")
        print(f"    Response Time: {result['response_time']}")
    if result['error']:
        print(f"    Error: {result['error']}")

# Summary
up_count = sum(1 for r in results if r['status'] == 'UP')
print(f"\nHealth Check Summary: {up_count}/{len(results)} services UP")

print()

# ========================================
# Exercise 10: API Integration - Weather Check
# ========================================
print("=" * 50)
print("Exercise 10: Public API Integration")
print("=" * 50)

# TODO: Using a public API (no auth required)
print("Fetching random user data:")
try:
    response = requests.get("https://randomuser.me/api/", timeout=10)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]

        print(f"\nRandom User Generated:")
        print(f"  Name: {user['name']['first']} {user['name']['last']}")
        print(f"  Email: {user['email']}")
        print(f"  Country: {user['location']['country']}")
        print(f"  Phone: {user['phone']}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

except requests.RequestException as e:
    print(f"Error: {e}")

print()

# ========================================
# Exercise 11: Downloading Files
# ========================================
print("=" * 50)
print("Exercise 11: Downloading Files")
print("=" * 50)

# TODO: Download a small file
print("Downloading a sample JSON file:")
try:
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        # Save to file
        filename = "downloaded_posts.json"
        with open(filename, 'w') as f:
            json.dump(response.json(), f, indent=2)

        print(f"Downloaded and saved to: {filename}")
        print(f"File size: {len(response.content)} bytes")

        # Clean up
        import os
        os.remove(filename)
        print(f"Cleaned up: {filename}")
    else:
        print(f"Download failed: {response.status_code}")

except requests.RequestException as e:
    print(f"Error downloading file: {e}")

print()

# ========================================
# Exercise 12: Session Management
# ========================================
print("=" * 50)
print("Exercise 12: Using Sessions")
print("=" * 50)

# TODO: Use session for multiple requests
print("Making multiple requests with session:")
with requests.Session() as session:
    # Set default headers for all requests in this session
    session.headers.update({'User-Agent': 'DevOps-Bootcamp/1.0'})

    # Make multiple requests
    for i in range(1, 4):
        response = session.get(f"https://jsonplaceholder.typicode.com/posts/{i}")
        if response.status_code == 200:
            post = response.json()
            print(f"  Post {i}: {post['title'][:40]}...")

print("\n" + "=" * 50)
print("Lab 5 Complete!")
print("=" * 50)

# ========================================
# Your Tasks:
# ========================================
"""
1. Make a GET request to https://api.github.com/users/YOUR_USERNAME and print your profile info

2. Create a function that checks if a website is up (returns True/False) with proper error handling

3. Write code that POSTs data to an API and handles different status codes appropriately

4. Create a health check script that:
   - Checks multiple service endpoints
   - Measures response time
   - Returns a summary report
   - Sends an alert if any service is down

5. Write a function that downloads a file from a URL with:
   - Progress indication
   - Timeout handling
   - Error handling

6. Create an API client class for JSONPlaceholder that:
   - Has methods for GET, POST, PUT, DELETE
   - Handles errors gracefully
   - Includes logging

7. Write code that makes parallel requests to multiple endpoints and collects results

8. Create a script that:
   - Fetches data from a public API
   - Transforms the data
   - Sends it to another API endpoint

9. Implement retry logic for failed requests (retry 3 times with exponential backoff)

10. Build a monitoring script that:
    - Checks API endpoints every 30 seconds
    - Logs response times
    - Alerts if response time > threshold
    - Saves results to a file
"""