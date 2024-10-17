import requests

def make_request():
    url = "https://retrieval-be.onrender.com"
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    make_request()
