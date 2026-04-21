from flask import Flask, render_template
# from database import all_products, all_sales

# creating an app instance
app = Flask(__name__)
# _name_ => tells where your app is located


@app.route('/')  # decorator function
def home():  # view fuction
    return render_template("index.html")


@app.route('/products')
def products():
    # products_data = all_products()
    return render_template("products.html")


@app.route('/sales')
def sales():
    # sales_data = all_sales()
    return render_template("sales.html")


@app.route('/stock')
def stock():
    return render_template("stock.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


app.run()
