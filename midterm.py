from flask import Flask, request, redirect, jsonify  # type: ignore

app = Flask(__name__)

# Sample dictionary of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30},
]

# Home route
@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐍 Flask 3-in-1 Demo</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        button { margin: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <h1>Welcome to this Python Website</h1>
    <h4>With the use of Flask!</h4>
    <form action="/passwordGame" method="get">
        <button type="submit">Method 1</button>
    </form>
    <form action="/dataRequest" method="get">
        <button type="submit">Method 2</button>
    </form>
    <form action="/patcher" method="get">
        <button type="submit">Method 3</button>
    </form>
</body>
</html>
    '''

# Method 1: Password protected page handler
@app.route('/passwordGame')
def password_game():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Guesser</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { margin: 10px; padding: 5px; }
        button { background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Password Guesser</h1>
    <h6>Hint: It's secret</h6>
    <form action="/login" method="post">
        <label for="password">Enter Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
    '''
@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    if password == 'secret': 
        return redirect('/logout')
    elif password == 'admin':
        return '''
        <h1>Welcome, Admin!</h1>
        <form action="/logout">
            <button type="submit">Logout</button>
        </form>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            button { margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        </style>
        '''
    else:
        return redirect('/error')
@app.route('/logout')
def logout():
    return '''
    You have successfully logged in! You can now go back.
    <form action="/">
        <button type="submit">Go Back</button>
    </form>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        button { margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
    '''
@app.route('/error')
def error():
    return '''
    You have entered an incorrect password.
    <form action="/passwordGame">
        <button type="submit">Try again!</button>
    </form>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        button { margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
    '''

# Method 2: Product Data Request
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 999},
    "2": {"name": "Book", "category": "Stationery", "price": 15},
    "3": {"name": "Headphones", "category": "Electronics", "price": 50}
}
@app.route('/dataRequest')
def data_request():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data Request</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { margin: 10px; padding: 5px; }
        button { background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Data Request</h1>
    <h6>Enter Product ID or Category</h6>
    <form action="/productDetails" method="get">
        <label for="id">Product ID:</label>
        <input type="text" id="id" name="id" placeholder="e.g., 1">
        <label for="category">Category (optional):</label>
        <input type="text" id="category" name="category" placeholder="e.g., Electronics">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
    '''
@app.route('/productDetails')
def product_details():
    product_id = request.args.get('id')
    category = request.args.get('category')
    if product_id and product_id in products:
        product = products[product_id]
        return f'''
        <h1>Product Details</h1>
        <p>Name: {product['name']}</p>
        <p>Category: {product['category']}</p>
        <p>Price: ${product['price']}</p>
        <form action="/">
            <button type="submit">Go Back</button>
        </form>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            button {{ margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }}
        </style>
        '''
    elif category:
        filtered_products = [p for p in products.values() if p['category'].lower() == category.lower()]
        if filtered_products:
            return f'''
            <h1>Products in Category: {category}</h1>
            <ul>
                {"".join([f"<li>{p['name']} - ${p['price']}</li>" for p in filtered_products])}
            </ul>
            <form action="/">
                <button type="submit">Go Back</button>
            </form>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
                button {{ margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }}
            </style>
            '''
        else:
            return '''
            <h1>No Products Found in This Category</h1>
            <form action="/">
                <button type="submit">Go Back</button>
            </form>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
                button {{ margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }}
            </style>
            '''
    else:
        return '''
        <h1>Product Not Found</h1>
        <form action="/">
            <button type="submit">Go Back</button>
        </form>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            button {{ margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }}
        </style>
        '''

# Method 3: Patching Users
@app.route('/patcher', methods=['GET', 'POST'])
def patcher():
    if request.method == 'POST':
        # Check if the form is for adding a new user or patching an existing one
        if 'new_name' in request.form:  # Adding a new user
            new_user = {
                "id": max([user['id'] for user in users]) + 1 if users else 1,  # Generate a new unique ID
                "name": request.form.get('new_name'),
                "email": request.form.get('new_email'),
                "age": int(request.form.get('new_age')) if request.form.get('new_age') else None
            }
            users.append(new_user)
        elif 'id' in request.form:  # Patching an existing user
            user_id = int(request.form.get('id'))
            user = next((u for u in users if u['id'] == user_id), None)
            if user:
                if request.form.get('name'):
                    user['name'] = request.form.get('name')
                if request.form.get('email'):
                    user['email'] = request.form.get('email')
                if request.form.get('age'):
                    user['age'] = int(request.form.get('age'))
    # Generate the table of users
    user_table = '''
    <table border="1" style="margin: 20px auto; border-collapse: collapse; width: 80%;">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Age</th>
            </tr>
        </thead>
        <tbody>
    '''
    for user in users:
        user_table += f'''
            <tr>
                <td>{user['id']}</td>
                <td>{user['name']}</td>
                <td>{user['email']}</td>
                <td>{user['age']}</td>
            </tr>
        '''
    user_table += '''
        </tbody>
    </table>
    '''
    # Return the page with the user table and forms
    return f'''
    <html>
    <head>
        <title>Patch or Add User</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            table {{ font-family: Arial, sans-serif; border: 1px solid #ddd; text-align: left; }}
            th, td {{ padding: 8px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            button {{ margin: 10px; padding: 5px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div style="display: flex; justify-content: space-around; align-items: flex-start; margin-top: 20px;">
    <!-- Patch User Form -->
    <div style="width: 45%; border: 1px solid #ddd; padding: 20px; border-radius: 5px;">
        <h1>Patch User</h1>
        <form method="POST">
            <label for="id">User ID:</label>
            <input type="number" id="id" name="id" required><br><br>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" placeholder="e.g., John"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="e.g., john@example.com"><br><br>
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" placeholder="e.g., 30"><br><br>
            <button type="submit">Patch User</button>
        </form>
    </div>
    <div style="width: 45%; border: 1px solid #ddd; padding: 20px; border-radius: 5px;">
        <h1>Add New User</h1>
        <form method="POST">
            <label for="new_name">Name:</label>
            <input type="text" id="new_name" name="new_name" placeholder="e.g., Jane" required><br><br>
            <label for="new_email">Email:</label>
            <input type="email" id="new_email" name="new_email" placeholder="e.g., jane@example.com" required><br><br>
            <label for="new_age">Age:</label>
            <input type="number" id="new_age" name="new_age" placeholder="e.g., 25"><br><br>
            <button type="submit">Add User</button>
        </form>
    </div>
</div>
<h2>Current Users</h2>
{user_table}
<form action="/">
    <button type="submit">Go Back</button>
</form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)