#!/usr/bin/python3
"""Module to learn how to develop an API using python's http.server module"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000


class APIhandler(BaseHTTPRequestHandler):
    """
    Basic HTTP request handler for simple API endpoints.

    Handles GET requests and returns:
        - "/" → Plain text greeting
        - "/data" → JSON sample data
        - "/status" → OK message
        - Other paths → 404 Not Found
    """
    def do_GET(self):
        """Handles incoming HTTP GET requests and sends the appropriate
        response."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(sample_data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found =(")


with HTTPServer(("", PORT), APIhandler) as httpd:
    print("serving at port : ", PORT)
    httpd.serve_forever()
