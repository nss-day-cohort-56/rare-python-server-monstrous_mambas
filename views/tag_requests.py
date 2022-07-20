import sqlite3
import json
from models import Tag


def get_all_tags():
    """get all tags
    """

    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER BY t.label ASC
        """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset: # we are fetching more than one b/c get all

            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return json.dumps(tags)

def create_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))  

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return json.dumps(new_tag)