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
        c.id category_id,
        c.label category_label,
        u.id user_id,
        u.first_name user_first_name,
        u.last_name user_last_name,
        u.email user_email,
        u.bio user_bio,
        u.username user_username,
        u.password user_password,
        u.profile_image_url user_profile_image_url,
        u.created_on user_created_on,
        u.active user_active

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
            category = Category(row['category_id'], row['category_label'])

            user = User(row['user_id'], row['user_first_name'], row['user_last_name'], row['user_email'], row['user_bio'], row['user_username'], row['user_password'], row['user_profile_image_url'], row['user_created_on'], row['user_active'])


            post.category =  category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)
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
        c.id category_id,
        c.label category_label,
        u.id user_id,
        u.first_name user_first_name,
        u.last_name user_last_name,
        u.email user_email,
        u.bio user_bio,
        u.username user_username,
        u.password user_password,
        u.profile_image_url user_profile_image_url,
        u.created_on user_created_on,
        u.active user_active

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
        category = Category(data['category_id'], data['category_label'])
        user = User(data['user_id'], data['user_first_name'], data['user_last_name'], data['user_email'], data['user_bio'], data['user_username'], data['user_password'], data['user_profile_image_url'], data['user_created_on'], data['user_active'])
        post.category = category.__dict__
        post.user = user.__dict__

        return json.dumps(post.__dict__)

def get_posts_by_user_id(id):
    """Get posts by user_id"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

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
            c.id category_id,
            c.label category_label,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url user_profile_image_url,
            u.created_on user_created_on,
            u.active user_active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.user_id = ?
        """, ( id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for data in dataset:
            post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'], data['content'], data['approved'])

            category = Category(data['category_id'], data['category_label'])

            user = User(data['user_id'], data['user_first_name'], data['user_last_name'], data['user_email'], data['user_bio'], data['user_username'], data['user_password'], data['user_profile_image_url'], data['user_created_on'], data['user_active'])

            post.category =  category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)
        
def delete_post(id):
    """delete a post
    """

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))

def create_new_post(new_post):

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

def edit_post(id, new_post):
    """
    whats happening here?
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'],
            new_post['image_url'], new_post['content'], new_post['approved'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_posts_by_category(category_id):
    """Get posts by category_id"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

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
            c.id category_id,
            c.label category_label,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url user_profile_image_url,
            u.created_on user_created_on,
            u.active user_active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.category_id = ?
        """, ( category_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for data in dataset:
            post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'], data['content'], data['approved'])

            category = Category(data['category_id'], data['category_label'])

            user = User(data['user_id'], data['user_first_name'], data['user_last_name'], data['user_email'], data['user_bio'], data['user_username'], data['user_password'], data['user_profile_image_url'], data['user_created_on'], data['user_active'])

            post.category =  category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)

def get_posts_by_title(search):
    """Get posts by title"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

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
            c.id category_id,
            c.label category_label,
            u.id user_id,
            u.first_name user_first_name,
            u.last_name user_last_name,
            u.email user_email,
            u.bio user_bio,
            u.username user_username,
            u.password user_password,
            u.profile_image_url user_profile_image_url,
            u.created_on user_created_on,
            u.active user_active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.title LIKE ?
        """, ( f"%{search}%", ))

        posts = []
        dataset = db_cursor.fetchall()

        for data in dataset:
            post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'], data['content'], data['approved'])

            category = Category(data['category_id'], data['category_label'])

            user = User(data['user_id'], data['user_first_name'], data['user_last_name'], data['user_email'], data['user_bio'], data['user_username'], data['user_password'], data['user_profile_image_url'], data['user_created_on'], data['user_active'])

            post.category =  category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)