from flask import Flask
from flask import render_template, request
from app.webhook import respond


app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello World'


@app.route('tt')
def index():
    return render_template("/templates/index.html")


@app.route('/webhook', methods=['POST'])
def dialogflow_webhook():
    json_dict = request.get_json()
    return respond(json_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
