from flask import Flask, render_template, request, redirect, url_for
from database import cur, all_sales, get_stock, all_products, get_user, insert_products, insert_sales, insert_stock


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
        print("product added successfully")
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = all_sales()
    return render_template("sales.html", sales=sales_data)


@app.route('/add_sales', methods=['GET', 'POST'])
def add_sales():
    if request.method == 'POST':
        products_id = int(request.form['p_id'])
        quantity = int(request.form['quantity'])
        insert_sales(products_id, quantity)
        print('sale added successfully')
    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock_data = get_stock()
    return render_template("stock.html", stock=stock_data)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        products_id = int(request.form['p_id'])
        stock_quantity = int(request.form['s_quantity'])
        new_stock = (products_id, stock_quantity)
        insert_stock(new_stock)
        print('stock added successfully')
    return redirect(url_for('stock'))


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    cur.execute("SELECT COALESCE(SUM(total), 0) FROM sales")
    total_sales = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM products")
    total_products = cur.fetchone()[0]

    cur.execute("SELECT * FROM products WHERE stock < 5")
    low_stock = cur.fetchall()

    return render_template(
        "dashboard.html",
        sales=total_sales,
        products=total_products,
        low_stock=low_stock
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(username, password)

        if user:
            session['user'] = username
            return redirect('/dashboard')

        else:
            message = "Invalid credentials"

    return render_template("login.html", message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        create_user(username, password)
        message = "Account created successfully"

    return render_template("register.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
