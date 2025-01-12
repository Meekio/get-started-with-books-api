import streamlit as st
import requests

base_url = "https://simple-books-api.glitch.me"
bearer_token = "xxx"

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
        st.success(response.json())
    else:
        st.error(response.json())

# GET bring list of all books on database
def get_books():
    response = requests.get(base_url + '/books')
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.json())

# POST place a book order
def place_order(book_id, customer_name):
    data = {
            "bookId": book_id,
            "customerName": customer_name
        }
    headers = {
        "Authorization": "Bearer xxx"
    }
    response = requests.post(base_url + '/orders', json=data, headers=headers)
    if response.status_code == 201:
        print(response.json())
    else:
        print(response.status_code, response.json())

st.title("Simple API Books interface")

st.header("Register User")
client_name = st.text_input("What is your name")
client_email = st.text_input("What is your email")
if st.button("Register"):
    response = register_user(client_email, client_name)

