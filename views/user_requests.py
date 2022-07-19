import sqlite3
from models import User

USERS = [
    {
        "id": 1,
        "first_name": "Syndney",
        "last_name": "Dickson",
        "bio": "I am a rockstar",
        "username": "syd",
        "img": "",
        "email": "sydrocks@gmail.com",
        "password": "123"
    },
    {
        "id": 2,
        "first_name": "Camille",
        "last_name": "Faulkner",
        "bio": "I am a powerhouse",
        "username": "cam",
        "img": "",
        "email": "camrocks@gmail.com",
        "password": "345"
    },
    {
        "id": 3,
        "first_name": "Connor",
        "last_name": "Lopshire",
        "bio": "I am an organizer",
        "username": "con",
        "img": "",
        "email": "conrocks@gmail.com",
        "password": "567"
    },
    {
        "id": 4,
        "first_name": "Claire",
        "last_name": "Morgan-Sanders",
        "bio": "I am a code genious",
        "username": "morg",
        "img": "",
        "email": "morgrocks@gmail.com",
        "password": "789"
    },
    {
        "id": 5,
        "first_name": "Tiana",
        "last_name": "Robinson",
        "bio": "I am a goof",
        "username": "tia",
        "img": "",
        "email": "tiarocks@gmail.com",
        "password": "901"
    },
]

def get_single_user(id):
    """
    get individual user
    """
    # Variable to hold the found user, if it exists
    requested_user = None

    # Iterate the userS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for user in USERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if user["id"] == id:
            requested_user = user

    return requested_user

def get_all_users():
    """
    get all employees
    """
    return USERS