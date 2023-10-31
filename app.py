from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/shop')
def shop():
    products = [
        {'id': 1, 'name': 'Product 1', 'price': 10.99},
        {'id': 2, 'name': 'Product 2', 'price': 19.99},
        {'id': 3, 'name': 'Product 3', 'price': 7.99}
    ]
    return render_template('shop.html', products=products)


@app.route('/checkout', methods=['POST'])
def checkout():
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])

    # Process payment logic here

    return 'Payment successful!'

if __name__ == '__main__':
    app.run(debug=True)
