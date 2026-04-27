# # cur.execute("select * from products")
# # products = cur.fetchall()
# # print(products)
# # cur.execute("select * from sales")
# # sales = cur.fetchall()
# # print(sales)
# # cur.execute("select * from stock")
# # stock = cur.fetchall()
# # print(stock)


# # def the_stock():
# #     cur = conn.cursor()
# #     cur.execute("select *  from stock")
# #     stock = cur.fetchall()
# #     return stock


# # print(the_stock())


# def get_data(table):
#     cur.execute(f"select * from {table}")
#     data = cur.fetchall()
#     return data


# products = get_data('products')
# print(products)


# def insert_products(product_details):
#     cur.execute(
#         "INSERT INTO products (name, buying_price, selling_price) VALUES (%s, %s, %s)",
#         product_details
#     )
#     conn.commit()


# product1 = ('HP laptop', 43000, 60000)
# product2 = ('Dell monitor', 55000, 75000)

# insert_products(product1)
# insert_products(product2)

# # def insert_sales(sales_details):
#     cur.execute(
#         f"insert into sales(products_id,quantity)values{sales_details}")
#     conn.commit()


# sales1 = (10, 5)
# sales2 = (1, 3)

# insert_sales(sales1)
# insert_sales(sales2)


# def insert_stock(stock_details):
#     cur.execute(
#         f"insert into stock(products_id,stock_quantity)values{stock_details}")
#     conn.commit()


# stock1 = (6, 4)
# stock2 = (8, 2)

# insert_stock(stock1)
# insert_stock(stock2)


# def insert_users(users_details):
#     cur.execute(
#         f"insert into users(full_name,email,phone_number,password)values{users_details}")
#     conn.commit()


# user1 = ('Regina W.', 'reggy@gmail.com', '0786541211', 'pass786')
# user2 = ('Fidelia Wambui', 'wambu@gmail.com', '0798453210', 'pass434')

# insert_users(user1)
# insert_users(user2)

# TASK
# 2.Write sql queries to fetch the following:
# (i)sales_per_product
# select products.name, sum(products.selling_price * sales.quantity) as total_sales from products join sales on products.id = sales.products_id group by products.name;
# (ii)sales_per_day
# select date(sales.created_at) as day, sum(products.selling_price * sales.quantity) as total_sales from products join sales on products.id = sales.products_id group by day;
# (iii)profit_per_product
# select products.name, sum(selling_price-buying_price) as profit from products group by products.name
# (iv)sales_per_day
# select date(sales.created_at) as day, sum(selling_price-buying_price)as total_profit from products join sales on products.id = sales.products_id group by day;


# def sales_per_product():
#     cur.execute('''select products.name, sum(products.selling_price * sales.quantity) as total_sales from products join sales on products.id = sales.products_id group by products.name;''')
#     product_sales = cur.fetchall()
#     return product_sales


# def sales_per_day():
#     cur.execute("""select date(sales.created_at) as day, sum(products.selling_price * sales.quantity) as total_sales from products join sales on products.id = sales.products_id group by day;""")
#     inday_sales = cur.fetchall()
#     return inday_sales


# def profit_per_product():
#     cur.execute(
#         """select products.name, sum(selling_price-buying_price) as profit from products group by products.name;""")
#     product_profit = cur.fetchall()
#     return product_profit


# def profit_per_day():
#     cur.execute("""select date(sales.created_at) as day, sum(selling_price-buying_price)as total_profit from products join sales on products.id = sales.products_id group by day;
# """)
#     inday_profit = cur.fetchall()
#     return inday_profit


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


def insert_sales(product_id, quantity):
    # get product price and stock
    cur.execute(
        "SELECT selling_price, stock FROM products WHERE id=%s", (product_id,))
    product = cur.fetchone()

    if not product:
        return "Product not found"

    price, stock = product

    if quantity > stock:
        return "Not enough stock"

    total = price * quantity

    # insert sale
    cur.execute("""
        INSERT INTO sales (product_id, quantity, total)
        VALUES (%s, %s, %s)
    """, (product_id, quantity, total))

    # reduce stock
    cur.execute("""
        UPDATE products
        SET stock = stock - %s
        WHERE id = %s
    """, (quantity, product_id))

    conn.commit()
    return "Sale successful"


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
