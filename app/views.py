from flask import render_template, request
from app.webhook import respond
from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/webhook', methods=['POST'])
def dialogflow_webhook():
    json_dict = request.get_json()
    print(json_dict)
    return respond(json_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
