#!/usr/bin/python3
""" Module to learn how to use simple API with flask """


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Lists all users saved in data"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user_info(username):
    """Lists data about specific user"""
    if users.get(username):
        return jsonify(users.get(username))
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def user_add():
    """adding a new user with value through curl request"""
    new_user = request.get_json()

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[new_user["username"]] = {
            "username": new_user["username"],
            "name": new_user["name"],
            "age": new_user["age"],
            "city": new_user["city"]
        }
        return jsonify({"message": "User added",
                        "user": users[new_user["username"]]}), 201


if __name__ == "__main__":
    app.run()
