


class Post():
    """Initialize a new post class w/ 8 parameters"""
    def __init__(self, id, title, user_id, category_id, publication_date, image_url, content, approved):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
