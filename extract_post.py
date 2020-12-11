import requests
import json


MEDIUM_API = "https://api.rss2json.com/v1/api.json"
MEDIUM_HANDLER = "@anitaokoh"


rss_url = "https://medium.com/feed/{}".format(MEDIUM_HANDLER)
response = requests.get(url=MEDIUM_API, params={"rss_url": rss_url},)
json_response = json.loads(response.text)

def fetch_content(story_json):
    return {item['title']:item["description"] for item in story_json["items"]}

def get_content():
    returned_content = fetch_content(json_response)
    content = list(returned_content.items())[7]
    return content



if __name__ == "__main__":
    get_content()