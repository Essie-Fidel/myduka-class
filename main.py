from flask import Flask, render_template, request, redirect, session
from database import cur, insert_products, insert_sales, get_stock, all_products, get_user


# creating an app instance
app = Flask(__name__)
# _name_ => tells where your app is located
app.secret_key = "myduka_secret_key"


@app.route('/')  # decorator function
def home():  # view fuction
    return render_template("index.html")


@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form['name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock = request.form['stock']

        insert_products(name, buying_price, selling_price, stock)
        return redirect('/products')

    products_data = all_products()
    return render_template("products.html", products=products_data)


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])

        insert_sales(product_id, quantity)
        return redirect('/sales')

    products = all_products()
    return render_template("sales.html", products=products)


@app.route('/stock')
def stock():
    stock_data = get_stock()
    return render_template("stock.html", stock=stock_data)


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
