from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_posts_url = "https://api.npoint.io/5abcca6f4e39b4955965"
response = requests.get(blog_posts_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_posts)

@app.route('/post/<int:blog_id>')
def blog_post_page(blog_id):
    return render_template("post.html", post_info=all_posts[blog_id])

if __name__ == "__main__":
    app.run(debug=True)
