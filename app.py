import requests

base_url = "https://simple-books-api.glitch.me"

# GET status
def get_status():
    response = requests.get(base_url + '/status')
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.json())

if __name__ == '__main__':
    get_status()