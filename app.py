# import flask
from flask import Flask, render_template
import requests, json
from random import *
import os, re, os.path

# create an app instance
app = Flask(__name__)
# create a route /
@app.route("/")     
# define the function hello             
def hello():
   # return "hello world" when
   return "Hello World!"

@app.route("/getnews")     
# define the function hello             
def getnews(stories=["tesla", "apple", "alphabet", "microsoft", "amazon", "google", "samsung", "facebook", "alibaba", "softbank"]):
    files = []
    token = 'e5c01c19612b4cd98b926ccda50fb7c1'
    for x in stories:
        fileint = randint(100000, 999999)
        query = 'https://newsapi.org/v2/everything?q={}&from=2021-11-14&sortBy=publishedAt&apiKey={}'.format(x, token)
        story = requests.get(query)
        filename = "/tmp/{}_{}.txt".format(x, fileint)
        files.append(filename)
        with open(filename, 'w') as outfile:
            outfile.write(str(story.content))
    return "got all news in {}".format(files)

@app.route("/deletenews")     
# define the function hello             
def deletenews():
    for root, dirs, files in os.walk("/tmp/"):
        for file in files:
            os.remove(os.path.join(root, file))
    return "cleared news from /tmp"


# on running python app.py
if __name__ == "__main__":
   # run the flask app
   app.run()
