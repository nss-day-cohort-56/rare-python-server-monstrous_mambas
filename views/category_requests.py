import sqlite3
import json
from models import Category

def get_all_categories():
    """convert each row into an category instance,
    convert the list to JSON, and respond to the client request"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        ORDER BY c.label ASC
        """)

        # Initialize an empty list to hold all category representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an category instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # category class above.
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(categories)


def get_single_category(id):
    """Get single category details"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        category = Category(data['id'], data['label'])

        return json.dumps(category.__dict__)
        