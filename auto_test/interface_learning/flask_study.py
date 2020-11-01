from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def login():
    data = json.dumps({
        "username":"lyz",
        "password":"123"
    })
    return data

if __name__ == '__main__':
    app.run()