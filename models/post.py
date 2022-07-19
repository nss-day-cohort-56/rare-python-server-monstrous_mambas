


class Post():
    def __init__(self, id, title, user_id, category_id, publication_date, img_url, content, approved):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.img_url = img_url
        self.content = content
        self.approved = approved
