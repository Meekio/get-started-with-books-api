import requests

base_url = "https://simple-books-api.glitch.me"

# GET status
def get_status():
    response = requests.get(base_url + '/status')
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.json())

# POST register user on the books API to obtain bearer token
def register_user(client_mail, client_name):
    data = {
        "clientName": client_name,
        "clientEmail": client_mail
    }
    response = requests.post(base_url + '/api-clients', json=data)
    if response.status_code == 201:
        print(response.json())
    else:
        print(response.status_code, response.json())


if __name__ == '__main__':
    get_status()
    register_user("honeybeeboo@gmail.com", "Jocelyn")