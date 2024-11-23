from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Test route
@app.route('/')
def home():
    return "Welcome to the Testing Flask App!"

# Example of dynamic route
@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

# Example of handling POST requests
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Assuming JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"message": "Data received", "data": data}), 200

# Example of rendering an HTML template
@app.route('/template')
def template():
    return render_template('index.html', title="Testing Flask App")

# Custom error handler
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
