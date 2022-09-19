import flask
from flask import Flask, render_template
import utils
import os
import sys

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask("Score")

@app.route('/')
def score_server():
    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')
        app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    else:
        app = Flask("Score")
    try:
        file = open(f"{utils.get_score_file_name()}", "r")
        SCORE = file.readline()
        file.close()
    except PermissionError:
        print("No permission to edit score")
        ERROR=utils.bad_return()
        return render_template('error.html', title='Scores Game', ERROR=ERROR)
    except FileNotFoundError:
        print("No score file")
        ERROR=utils.bad_return()
        return render_template('error.html' , title='Scores Game', ERROR=ERROR)
    return render_template('index.html', title='Scores Game', SCORE=SCORE)

app.run(host="0.0.0.0", port=5001, debug=False)


