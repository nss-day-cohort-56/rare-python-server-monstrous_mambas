from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views.posttags_requests import create_posttag, delete_posttag, edit_posttag, get_all_posttags, get_all_tags_for_post
from views.tag_requests import create_tag, get_all_tags
from views.post_request import delete_post, edit_post, get_all_post, get_posts_by_category, get_single_post, create_new_post, get_posts_by_user_id, get_posts_by_category
from views import get_all_categories, get_single_category, get_all_users, create_category, delete_category, get_posts_by_title
from views.user_requests import create_user, login_user, get_single_user
from views.comment_requests import create_new_comment, get_all_comments_by_id


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        path_params = path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def do_GET(self):
        """Handle Get requests to the server"""

        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            elif resource == "tags": 
                    response = f"{get_all_tags()}"
            elif resource == "posts":
                    if id is not None:
                        response = f"{get_single_post(id)}"
                    else:
                        response = f"{get_all_post()}"
            elif resource == "users": 
                    if id is not None:
                        response = f"{get_single_user(id)}"
                    else:
                        response = f"{get_all_users()}"
            elif resource == "posttags": 
                    response = f"{get_all_posttags()}"

        else:
            ( resource, query, id ) = parsed

            if query == 'user_id' and resource == 'posts':
                response = get_posts_by_user_id(id)
            elif query == 'category_id' and resource == 'posts':
                response = get_posts_by_category(id)
            elif query == 'post_id' and resource == 'comments':
                response = get_all_comments_by_id(id)
            elif query == 'post_id' and resource == 'posttags':
                response = get_all_tags_for_post(id)
            elif query == 'title' and resource == 'posts':
                response = get_posts_by_title(id)

        self.wfile.write(response.encode())


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, id) = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            response = create_category(post_body)
        if resource == "tags":
            response = create_tag(post_body)
        if resource == "posts":
            response = create_new_post(post_body)
        if resource == "posttags":
            response = create_posttag(post_body)
        if resource == "comments":
            response = create_new_comment(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "posts":
            success = edit_post(id, post_body)
        elif resource == "posttags":
            success = edit_posttag(id, post_body)
        # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
        pass

    def do_DELETE(self):
        """Handle DELETE Requests"""

        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single entry from the list
        if resource == "categories":
            delete_category(id)
        elif resource == "posts":
            delete_post(id)
        elif resource == "posttags":
            delete_posttag(id)

        # Encode the new entry and send in response
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
