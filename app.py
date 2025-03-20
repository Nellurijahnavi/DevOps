from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Registration Page!"

# Registration form route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Print the form data (for demonstration purposes)
        print(f"User {username} registered with email {email}")

        # Show a success message on the registration page
        return f"Successfully registered! Welcome, {username}!"

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)


