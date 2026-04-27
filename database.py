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


def insert_users(users_details):
    cur.execute(
        "insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)", (users_details))
    conn.commit()


user1 = ('Regina W.', 'reggy@gmail.com', '0786541211', 'pass786')
user2 = ('Fidelia Wambui', 'wambu@gmail.com', '0798453210', 'pass434')

# insert_users(user1)
# insert_users(user2)


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


product3 = ('Samsung TV', 85000, 110000)
product4 = ('Wireless Mouse', 800, 1500)

insert_products(product3)
insert_products(product4)


def all_products():
    cur = conn.cursor()
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


print(all_products())


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


print(all_sales())


def get_stock():
    cur.execute("SELECT * FROM stock")
    return cur.fetchall()


def get_user(username, password):
    cur.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    return cur.fetchone()


def create_user(username, password):
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()
