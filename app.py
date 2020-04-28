from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/menu')
def index_menu():
    return '<h1>Menu</h1>'

@app.route('/menu/<id>')
def menu_item(id):
    return '</h1>Menu Item: {}</h1>'.format(id)

@app.route('/account')
def account():
    account_id = 'test-account'
    return render_template('account.html', account_id=account_id)

@app.route('/orders')
def orders():
    orders = [
        {
            'id': 1,
            'title': 'order 1',
            'details': 'a lot of food'
        },
        {
            'id': 2,
            'title': 'order 2',
            'details': 'a lot of food again'
        },
    ]
    return render_template('orders.html', orders=orders)

@app.route('/order/<id>')
def order(id):
    return '<h1>Order {}</h1>'.format(id)


if __name__ == '__main__':
    app.run(debug=True)
