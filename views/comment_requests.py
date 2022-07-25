import sqlite3
import json
from models import Comment


def get_all_comments_by_id(id):
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
        c.id,
        c.post_id,
	    c.author_id,
	    c.content
    FROM Comments c
    Where post_id = ?
        """, (id, ))

        # Initialize an empty list to hold all category representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an category instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # category class above.
            comment = Comment(row['id'], row['post_id'],
                            row['author_id'], row['content'])

            comments.append(comment.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(comments)


def delete_comment(id):
    """delete a comment
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))


def create_new_comment(new_comment):

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ? );
        """, (new_comment['post_id'], new_comment['author_id'],
            new_comment['content'] ))

        id = db_cursor.lastrowid

        new_comment['id'] = id

    return json.dumps(new_comment)