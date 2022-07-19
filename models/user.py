from datetime import date

class User():
    """
    template for user representaion
    """

    def __init__(self, id, first_name, last_name, bio, username, email = "", password = ""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.username  = username
        self.img = ""
        self.email = email
        self.password = password
        self.date_added = date.today()
