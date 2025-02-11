from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_text')
def fetch_text():
    return jsonify(text="Hello, you've clicked the button!")

if __name__ == '__main__':
    app.run(debug=True)
