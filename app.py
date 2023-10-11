# post_service.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)
posts = {
    '1': {'user_id': '1', 'post': 'Hello, world!'},
    '2': {'user_id': '2', 'post': 'My first blog post'}
}


@app.route('/')
def index():
    return 'post server up and running'

@app.route('/post/<id>')
def post(id):

    post_info = posts.get(id, {})
    
    # Get user info from User Service
    if post_info:
        response = requests.get(f'https://userservice.ashyrock-0da57b89.canadacentral.azurecontainerapps.io/user/{post_info["user_id"]}')
        if response.status_code == 200:
            post_info['user'] = response.json()

    return jsonify(post_info)
# create post
@app.route('/create_post/<post_id>/<user_id>/<post>')
def create_post(post_id, user_id, post):
    posts[post_id] = {'user_id': user_id, 'post': post}
    return jsonify(posts)

# update post
@app.route('/update_post/<id>/<user_id>/<post>')
def update_post(id, user_id, post):
    posts[id] = {'user_id': user_id, 'post': post}
    return jsonify(posts)

# delete post
@app.route('/delete_post/<id>')
def delete_post(id):
    if id in posts:
        del posts[id]
        return jsonify(posts)
    else:
        return 'post not found'


if __name__ == '__main__':
    app.run()