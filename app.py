# post_service.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/post/<id>')
def post(id):
    posts = {
        '1': {'user_id': '1', 'post': 'Hello, world!'},
        '2': {'user_id': '2', 'post': 'My first blog post'}
    }
    post_info = posts.get(id, {})
    
    # Get user info from User Service
    if post_info:
        response = requests.get(f'https://userservice.ashyrock-0da57b89.canadacentral.azurecontainerapps.io/user/{post_info["user_id"]}')
        if response.status_code == 200:
            post_info['user'] = response.json()

    return jsonify(post_info)

if __name__ == '__main__':
    app.run()