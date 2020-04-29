from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/thankyou')
def thank_you():
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    username = request.args.get('username')
    # username must contain lowercase letter
    # username must contain uppercase letter
    # username must end in a number
    lower_letter = False
    upper_letter = False
    num_end = False

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    errors = []
    if not num_end:
        errors.append('Username must end in a number')

    if not lower_letter:
        errors.append('Username must containe a lowercase letter')
    
    if not upper_letter:
        errors.append('Username must contain an uppercase letter')

    return render_template('thankyou.html', first_name=first_name, errors=errors)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def index_menu():
    return render_template('menu.html')

@app.route('/menu/<id>')
def menu_item(id):
    return '</h1>Menu Item: {}</h1>'.format(id)

@app.route('/account')
def account():
    user_logged_in = False
    account_id = 'test-account'
    return render_template('account.html', account_id=account_id, user_logged_in=user_logged_in)

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
