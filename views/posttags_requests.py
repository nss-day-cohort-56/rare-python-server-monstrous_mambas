import sqlite3
import json
from models import Tag
from models.post import Post
from models.posttag import PostTag


def get_all_posttags():
    """get all post tags
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        """)

        posttags = []

        dataset = db_cursor.fetchall()
        for row in dataset:  # we are fetching more than one b/c get all
            posttag = PostTag(row['id'], row['post_id'], row['tag_id'])
            posttags.append(posttag.__dict__)

    return json.dumps(posttags)


def create_posttag(new_posttag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            ( post_id, tag_id )
        VALUES
            ( ?, ? );
        """, (new_posttag['post_id'], new_posttag['tag_id'],))

        id = db_cursor.lastrowid

        new_posttag['id'] = id

    return json.dumps(new_posttag)


def get_all_tags_for_post(id):
    """Get all tags associated with a post"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
        p.id post_id,
        pt.id posttag_id,
        pt.post_id,
        pt.tag_id,
        t.id tag_id,
        t.label

        FROM PostTags pt
        JOIN Tags t
            ON t.id = pt.tag_id
        JOIN Posts p
            ON p.id = pt.post_id
        WHERE pt.post_id = ?
        """, (id, ))

        # Initialize an empty list to hold all animal representations
        posttags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a post user and category instance from the current row
            posttag = PostTag(row['posttag_id'], row['post_id'], row['tag_id'])
            post = Post(row['post_id'])
            tag = Tag(row['tag_id'], row['label'])

            posttag.post = post.__dict__
            posttag.tag = tag.__dict__

            posttags.append(posttag.__dict__)


    return json.dumps(posttags)


def edit_posttag(id, new_post):
    """
    whats happening here?
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                post_id = ?,
                tag_id = ?
        WHERE id = ?
        """, (new_post['post_id'], new_post['tag_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def delete_posttag(id):
    """delete an entry
    """

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))