from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Return a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_username():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return the API status."""
    return "OK"


@app.route('/users/<username>')
def user(username):
    """Return user data for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary."""
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
