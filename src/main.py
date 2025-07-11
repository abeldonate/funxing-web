import os
import datetime
from flask import Flask, render_template, url_for

template_path = os.path.abspath("src/templates")
static_path = os.path.abspath("src/static")

app = Flask(
    __name__,
    template_folder=template_path,
    static_folder=static_path,
)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/maze')
def maze():
    return render_template('maze.html')

@app.route('/events')
def events():
    return render_template('events.html')


if __name__ == '__main__':
    app.run(port=5100, host='0.0.0.0')