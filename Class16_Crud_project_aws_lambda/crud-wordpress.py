import requests
from requests.auth import HTTPBasicAuth



# /wp-json/wp/v2/posts
# /wp-json/wp/v2/posts/{id}
url = "https://livingdevops.com"
your_username  = 'livingdevops'
your_password = 'T2Zs tAkI zBgD KoUO OEBs PELa'

# posts = requests.get(url + "/wp-json/wp/v2/posts")
# page = 1
# per_page = 1
# response = requests.get(url + "/wp-json/wp/v2/posts", params={"page": page, "per_page": per_page})

# print(response.json())
# for post in response.json():
#     print(f" LINK:{ post.get('link')}")
#     print(f" TITLE:{ post.get('title')['rendered']}")
#     print("----")

def list_posts(page=1, per_page=5):
    response = requests.get(url + "/wp-json/wp/v2/posts", params={"page": page, "per_page": per_page})
    for post in response.json():
        print(f" LINK:{ post.get('link')}")
        print(f" ID:{ post.get('id')}")
        print(f" TITLE:{ post.get('title')['rendered']}")
        print("----")

# print("---- Listing Posts with Pagination ----")
# list_posts(page=1, per_page=2)

def get_post(post_id):
    response = requests.get(url + f"/wp-json/wp/v2/posts/{post_id}")
    post = response.json()
    print(f" LINK:{ post.get('link')}")
    print(f" TITLE:{ post.get('title')['rendered']}")
    #print(f" CONTENT:{ post.get('content')['rendered']}")
    print("----")

# print("---- Getting Single Post ----")
# get_post(1777)

def create_post(title, content, status="draft"):
    data = {
        "title": title,
        "content": content,
        "status": status
    }
    response = requests.post(url + "/wp-json/wp/v2/posts", json=data, auth=HTTPBasicAuth(your_username, your_password))
    print(response.json())

# print("---- Creating a New Post ----")
# create_post("API Created Post - by Rajesh", "This post is created via REST API using Python", status="draft")


def update_post(post_id, title=None, content=None, status=None):
    data = {}
    if title:
        data["title"] = title
    if content:
        data["content"] = content
    if status:
        data["status"] = status

    response = requests.post(url + f"/wp-json/wp/v2/posts/{post_id}", json=data, auth=HTTPBasicAuth(your_username, your_password))
    print(response.json())

# print("---- Updating an Existing Post ----")
# update_post(1777, title="Updated Title via POST method", status="draft")  

def delete_post(post_id, force=True):
    response = requests.delete(url + f"/wp-json/wp/v2/posts/{post_id}", params={"force": str(force).lower()}, auth=HTTPBasicAuth(your_username, your_password))
    print(response.json())

# print("---- Deleting a Post ----")
# delete_post(1776)

def patch_post_title(post_id, title):
    data = {"title": title}
    response = requests.patch(url + f"/wp-json/wp/v2/posts/{post_id}", json=data, auth=HTTPBasicAuth(your_username, your_password))
    print(response.json())
    
# post_to_update = 1775
# update_post(post_to_update, title= "this is updating the post from patch method")
