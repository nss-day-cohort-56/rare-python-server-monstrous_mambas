import sqlite3
import json

from models.category import Category

from models.post import Post
from models.user import User


def get_all_post():
    """Get post details"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.label,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a post user and category instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                            row['publication_date'], row['image_url'], row['content'], row['approved'])
            category = Category(row['id'], row['label'])

            user = User(row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])


            post.category =  category.__dict__

            post.user = user.__dict__

    # Add the dictionary representation of the animal to the list
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)

def get_single_post(id):
    """Get single post details"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.label,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'], data['content'], data['approved'])
        category = Category(data['id'], data['label'])
        user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['bio'], data['username'], data['password'], data['profile_image_url'], data['created_on'], data['active'])
        post.category = category.__dict__
        post.user = user.__dict__

        return json.dumps(category.__dict__)
        
def create_new_post(new_post):
    """
    
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved)
        VALUES
            ( ?, ?, ?, ?, ?, ?, ? );
        """, (new_post['user_id'], new_post['category_id'],
            new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'])) 

        id = db_cursor.lastrowid

        new_post['id'] = id

    return json.dumps(new_post)

