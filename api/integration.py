
import requests

def api_get(url, data):
    response = requests.get(url, data=data)
    return response

def api_post(url, data):
    response = requests.post(url, data=data)
    return response

def api_put(url, data):
    response = requests.put(url, data=data)
    return response