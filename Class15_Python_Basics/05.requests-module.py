import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Json-place-holder-website Status code:", response.status_code)

# python -m venv .venv
# source .venv/bin/activate (for linux/mac)
# source .venv/Scripts/activate (for windows)
# pip install requests

print("---- Living DevOps Blog ----")
url = "https://livingdevops.com"
post_endpoint = "/wp-json/wp/v2/posts"
page_endpoint = "/wp-json/wp/v2/pages"

# response = requests.get(url, timeout=5)
# if response.status_code == 200:
#     print(response)

posts = requests.get(url + post_endpoint)
last_post = posts.json()[-1]
print('link: ', last_post['link'])
print('title: ', last_post['title']['rendered'])
#print(last_post.get('link'), last_post.get('title')["rendered"])

print("---- All Posts ----")
pages = requests.get(url + page_endpoint)
print("Total Pages:", len(pages.json()))
#print("Last Page:", pages.json()[-1])
print("Last Page Link:", pages.json()[-1]['link'])

#print(pages.json()[-1].get('link'))
print("")
print("---- All Pages Links and Title ----")
print("")
for page in pages.json():
    print(f" LINK:{ page.get('link')}")
    print(f" TITLE:{ page.get('title')["rendered"]}")
    #print("----")