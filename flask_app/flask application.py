import time
from random import choice
from string import ascii_letters, punctuation, digits

import flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    ip_adress = flask.request.remote_addr
    browser = request.user_agent.browser
    server_time = time.strftime('%A %B, %d %Y %H:%M:%S')
    return f"Browser: {browser}; Ip Adress: {ip_adress}; Server time: {server_time}."


@app.route('/source_code')
def source_code():
    f = open('app.py', 'r')
    text = str(f.readlines())
    f.close()

    return text


if __name__ == '__main__':
    app.run()


@app.route('/random')
def random_string_generator():
    length = int(request.args.get('length'))
    specials = int(request.args.get('specials'))
    digit = int(request.args.get('digits'))
    string = ''.join(choice(ascii_letters) for i in range(length))

    if length in range(1, 101) and specials in range(2) and digit in range(2):
        if specials == 1 and digit == 1:
            string = ''.join(choice(ascii_letters + punctuation + digits) for i in range(length))
        elif specials == 0 and digit == 0:
            return string
        elif specials == 1 and digit == 0:
            string = ''.join(choice(ascii_letters + punctuation) for i in range(length))
        elif specials == 0 and digit == 1:
            string = ''.join(choice(ascii_letters + digits) for i in range(length))
    else:
        string = 'Enter correct URL'

    return string
