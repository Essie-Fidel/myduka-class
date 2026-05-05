import psycopg2


conn = psycopg2.connect(host='localhost', port='5432',
                        user='postgres', password='2510', dbname='myduka_db')

cur = conn.cursor()


def insert_stock(stock_details):
    cur.execute(
        "insert into stock(products_id,stock_quantity)values(%s,%s)", (stock_details))
    conn.commit()


stock1 = (5, 2)
stock2 = (7, 4)

# insert_stock(stock1)
# insert_stock(stock2)


def insert_products(product_details):
    cur.execute(
        """
        INSERT INTO products (name, buying_price, selling_price)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING
        """,
        product_details
    )
    conn.commit()


def all_products():
    cur = conn.cursor()
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


# print(all_products())


def insert_sales(products_id, quantity):
    cur.execute("""
        INSERT INTO sales (products_id, quantity)
        VALUES (%s, %s)
    """, (products_id, quantity))
    conn.commit()


def all_sales():
    cur = conn.cursor()
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


# print(all_sales())


def get_stock():
    cur.execute("SELECT * FROM stock")
    return cur.fetchall()


def insert_user(users_details):
    cur.execute(
        "insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)", (users_details))
    conn.commit()


def get_user():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()


# how to check user using email


def check_user_exists(email):
    cur.execute(
        "SELECT * FROM users WHERE email = %s",
        (email,)
    )
    user = cur.fetchone()
    return user


def available_stock(p_id):
    cur.execute(
        "select sum(stock_quantity) from stock where products_id=%s", (p_id,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum (quantity) from sales where products_id=%s", (p_id,))
    total_sold = cur.fetchone()[0] or 0
    return total_stock-total_sold


# check_stock = available_stock(134)
# print(check_stock)
# check_stock = available_stock(34)
# print(check_stock)


def sales_per_product():
    cur.execute("""
        SELECT products.name,
               SUM(products.selling_price * sales.quantity) AS total_sales
        FROM products
        JOIN sales ON products.id = sales.products_id
        GROUP BY products.name;
    """)
    return cur.fetchall()


def sales_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS day,
               SUM(products.selling_price * sales.quantity) AS total_sales
        FROM products
        JOIN sales ON products.id = sales.products_id
        GROUP BY day
        ORDER BY day;
    """)
    return cur.fetchall()


def profit_per_product():
    cur.execute("""
        SELECT products.name,
               SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit
        FROM products
        JOIN sales ON products.id = sales.products_id
        GROUP BY products.name;
    """)
    return cur.fetchall()


def profit_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS day,
               SUM((products.selling_price - products.buying_price) * sales.quantity) AS total_profit
        FROM products
        JOIN sales ON products.id = sales.products_id
        GROUP BY day
        ORDER BY day;
    """)
    return cur.fetchall()
