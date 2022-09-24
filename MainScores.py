import flask
from flask import Flask, render_template
import utils
import os
import sys
app=Flask(__name__, template_folder='templates', static_folder='static')

def app_run(app):
    app.run(host="0.0.0.0", port=8777, debug=False)


@app.route('/')
def score_server():
    app_run(app)
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


