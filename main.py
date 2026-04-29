from flask import Flask, render_template, request, redirect, url_for, flash
from database import cur, all_sales, get_stock, all_products, insert_products, insert_sales, insert_stock, available_stock, insert_user


# creating an app instance
app = Flask(__name__)
# _name_ => tells where your app is located
app.secret_key = "myduka_secret_key"


@app.route('/')  # decorator function
def home():  # view fuction
    return render_template("index.html")


@app.route('/products')
def products():
    products_data = all_products()
    return render_template("products.html", products=products_data)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name, buying_price, selling_price)
        insert_products(new_product)
        flash('product added successully', 'success')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = all_sales()
    products_data = all_products()
    return render_template("sales.html", sales=sales_data, products=products_data)


@app.route('/add_sales', methods=['GET', 'POST'])
def add_sales():
    if request.method == 'POST':
        products_id = int(request.form['p_id'])
        quantity = int(request.form['quantity'])
        check_stock = available_stock(products_id)
        if check_stock < quantity:
            flash("insufficient stock can't complete sale", 'danger')
            return redirect(url_for('sales'))
        insert_sales(products_id, quantity)
        flash('sale added successfully', 'success')
    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = all_products()
    return render_template("stock.html", stock=stock_data, products=products_data)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        products_id = int(request.form['p_id'])
        stock_quantity = int(request.form['s_quantity'])
        new_stock = (products_id, stock_quantity)
        insert_stock(new_stock)
        flash('stock added successfully', 'success')
    return redirect(url_for('stock'))


@app.route('/register', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        full_name = request.form['f_name']
        email_address = request.form['email']
        phone_number = int(request.form['phone'])
        password = request.form['pass']
        new_user = (full_name, email_address, phone_number, password)
        insert_user(new_user)
        flash("Account created successfully!")
        return redirect(url_for('create_user'))
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
