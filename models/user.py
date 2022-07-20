from datetime import date

class User():
    """
    template for user representaion
    """

    def __init__(self, id, first_name, last_name, email, bio, username, password, profile_image_url, created_on = date.today(), active = 1 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.username  = username
        self.password = password
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active
