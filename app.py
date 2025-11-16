from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Мир')
    message = request.args.get('message', 'Привет!')
    return f"Hello {name}! {message}!"

if __name__ == '__main__':
    app.run()