from flask import Flask, escape, request

server = Flask(__name__)

@server.route('/')
def respond():
    return "what's up"

@server.route('/page')
def respondWithHTML():
    return "<h1>THIS IS HTML</h1>"

server.run(host="0.0.0.0", port=80)
