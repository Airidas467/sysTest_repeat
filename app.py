from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Hello route
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# Simple API POST route
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received": data})

if __name__ == "__main__":
    app.run(debug=True)
