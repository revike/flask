from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return Response(f'This is a {request.method} request')
    return Response(f'This is a {request.method} request')
