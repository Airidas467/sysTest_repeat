from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to your Flask app.</p>"

@app.route('/enter_invoice', methods=['GET', 'POST'])
def enter_invoice():
    if request.method == 'POST':
        invoice_number = request.form.get('invoice_number')
        return redirect(url_for('show_invoice', order=invoice_number))
    return render_template('enter_invoice.html')


@app.route('/showinvoice')
def show_invoice():
    order = request.args.get('order', '')
    return render_template('show_invoice.html', order=order)

if __name__ == '__main__':
    app.run(debug=True)
