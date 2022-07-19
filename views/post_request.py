import sqlite3
import json

from models.post import Post


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
        id,
        user_id,
        category_id,
        title,
        publication_date,
        image_url,
        content,
        approved

        FROM Posts 
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
          
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                            row['publication_date'], row['image_url'], row['content'], row['approved'])
    # Create a Location instance from the current row

    # Add the dictionary representation of the location to the animal
          
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
        p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        category = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'], data['content'], data['approved'])

        return json.dumps(category.__dict__)
        