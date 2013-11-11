import os
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect("http://www.meetup.com/PyLadiesDublin/")

if __name__ == "__main__":
    app.run(debug=True)
