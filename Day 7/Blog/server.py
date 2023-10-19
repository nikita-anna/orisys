from flask import Flask
from flask import render_template
import random
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_blogs=response.json()
#blog_title=response[0]["title"]
#blog_subtitle=response[0]["subtitle"]

app=Flask(__name__)
#random_number=random.randint(0,10)


@app.route('/')
def port():
    return render_template("post.html",post=all_blogs)
    #return render_template("post.html", title=blog_title, subtitle=blog_subtitle)

@app.route('/blog/<int:id>')
def blog(id):
    for blog in all_blogs:
        if blog["id"]==id:
            requested_blog=blog
    return render_template("index.html",posts=requested_blog)

@app.route('/bye/<name>')
def say_bye(name):
    return f"hey {name}"

if __name__=="__main__":
    app.run(debug=True)


#print(response[0]["title"])
#for post in response:
    #print(post["title"])
