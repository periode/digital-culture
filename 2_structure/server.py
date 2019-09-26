from flask import Flask, escape, request

server = Flask(__name__)

@server.route('/')
def respond():
    return "what's up"

server.run(host="0.0.0.0", port=80)
