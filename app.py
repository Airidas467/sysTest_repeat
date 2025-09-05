from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Dynamic route example
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to my Flask App.</p>"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
