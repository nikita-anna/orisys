from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    temp=["spotify.html","spotify.css"]
    return render_template(temp)
    
if __name__=="__main__":
    app.run(debug=True)