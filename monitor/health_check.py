import requests

def check_endpoint(url):

    try:
        response = requests.get(url, timeout=5)
        return response.status_code

    except Exception:
        return "FAILED"
