from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Hemant", "email": "desalehemant87@gmail.com"},
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Demo App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .user-card { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .form-group { margin: 15px 0; }
        input, button { padding: 8px; margin: 5px; }
        button { background: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flask Demo App</h1>
        <p>Welcome to this simple Flask application!</p>
        
        <h2>Users</h2>
        {% for user in users %}
        <div class="user-card">
            <strong>{{ user.name }}</strong><br>
            Email: {{ user.email }}
        </div>
        {% endfor %}
        
        <h2>Add New User</h2>
        <form method="POST" action="/add_user">
            <div class="form-group">
                <input type="text" name="name" placeholder="Name" required>
            </div>
            <div class="form-group">
                <input type="email" name="email" placeholder="Email" required>
            </div>
            <button type="submit">Add User</button>
        </form>
        
        <h2>API Endpoints</h2>
        <p>Try these API endpoints:</p>
        <ul>
            <li><a href="/api/users">/api/users</a> - Get all users (JSON)</li>
            <li><a href="/api/hello/YourName">/api/hello/YourName</a> - Personalized greeting</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page displaying users and a form to add new ones"""
    return render_template_string(HTML_TEMPLATE, users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via form submission"""
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        new_id = max([user['id'] for user in users]) + 1 if users else 1
        users.append({"id": new_id, "name": name, "email": email})
    
    return render_template_string(HTML_TEMPLATE, users=users)

@app.route('/api/users')
def api_users():
    """API endpoint to get all users as JSON"""
    return jsonify(users)

@app.route('/api/hello/<name>')
def api_hello(name):
    """API endpoint for personalized greeting"""
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success",
        "total_users": len(users)
    })

@app.route('/api/users/<int:user_id>')
def api_user_by_id(user_id):
    """API endpoint to get a specific user by ID"""
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page"""
    return "<h1>404 - Page Not Found</h1><p>The page you're looking for doesn't exist.</p>", 404

if __name__ == '__main__':
    print("Starting Flask app...")
    print("Visit: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)