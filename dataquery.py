import sqlite3

def get_product_details(id_product):
    # Connect to the database
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    
    # Query to get color and type based on id_product
    cursor.execute('''
    SELECT color, type FROM products WHERE id_product = ?
    ''', (id_product,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    if result:
        color, type = result
        return color, type
    else:
        return None, None
    
def get_color_affect(color):
    # Connect to the database
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    
    # Query to get the affect based on color by joining with effects table
    cursor.execute('''
    SELECT e.affect FROM effects e
    JOIN products p ON e.degree = (
        CASE
            WHEN p.color = ? THEN 1
            ELSE 4
        END
    )
    WHERE p.color = ?
    ''', (color, color))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    if result:
        return result[0]
    else:
        return None
    
def get_color_degree(color):
    conn = sqlite3.connect('product_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT degree FROM effects WHERE affect = (
            SELECT affect FROM products WHERE color = ?
        )
    ''', (color,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Take id_product as input
id_product = int(input("Enter the id_product: "))

# Get the product details
color, type = get_product_details(id_product)

if color and type:
    print(f'Product ID: {id_product}\nColor: {color}\nType: {type}')
else:
    print(f'Product with ID {id_product} not found.')

degree = get_color_degree(color)

if color and degree:
    # Get the color affect
    affect = get_color_affect(color)
    print(f'Affect: {affect}')
else:
    print(f'Product with ID {id_product} not found.')
