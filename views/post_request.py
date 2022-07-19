import sqlite3
import json

from models.post import Post


def get_all_post():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
        id
        user_id
        category_id
        title
        publication_date
        img_url
        content
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
                            row['publication_date'], row['img_url'], row['content'], row['approved'])
    # Create a Location instance from the current row

    # Add the dictionary representation of the location to the animal
          
    # Add the dictionary representation of the animal to the list
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)