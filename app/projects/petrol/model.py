import json
import urllib.request


def get_data():
    with urllib.request.urlopen("https://apis.is/petrol") as url:
        data = json.loads(url.read().decode())
        return data['results']
