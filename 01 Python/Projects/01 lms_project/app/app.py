from flask import Flask, render_template, request, flash, redirect, url_for, session
from db import create_connection  # db connection from dy.py
import os

# Create instance of Flask
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user:
                user_password = user[3]  # Assuming password is the 4th field
                if password == user_password:
                    session['user_email'] = email
                    flash("Login successful!", "success")
                    return redirect(url_for("dashboard"))  # Redirect to the dashboard
                else:
                    flash("Invalid password.", "error")
            else:
                flash("No user found with this email. Please create an account.")
                return render_template("register.html")
        else:
            flash("Connection not established.")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        country = request.form["country"]
        phone = request.form["phone"]
        dob = request.form["dob"]
        role = request.form["role"]

        # Access DataBase
        connection = create_connection()
        if connection:
            cursor = connection.cursor()

            # Insert user details into the database
            insertQuery = """
                        INSERT INTO users (first_name, last_name, email, password, country, phone, dob, role)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
            try:
                cursor.execute(insertQuery, (firstname, lastname, email, password, country, phone, dob, role))
                connection.commit()
                flash("Registration successful!", "success")
                return redirect(url_for("login"))
            except Exception as e:
                flash(f"An error occurred: {e}")
            finally:
                cursor.close()
                connection.close()
        else:
            flash("Failed to connect to the database.")
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if 'user_email' not in session:
        return redirect('/login')

    email = session['user_email']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user is None:
        flash("User not found.", "error")
        return redirect('/login')

    return render_template("dashboard.html", user=user)


@app.route("/edit_details", methods=["POST"])
def edit_details():
    if 'user_email' not in session:
        return redirect('/login')

    # Get form data
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    password = request.form["password"]
    country = request.form["country"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    role = request.form["role"]

    email = session['user_email']  # Get the user's email from the session

    # Database connection
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Corrected SQL query string
        updateQuery = """
            UPDATE users 
            SET first_name = %s, last_name = %s, password = %s, country = %s, phone = %s, dob = %s, role = %s
            WHERE email = %s
        """

        try:
            # Execute the query with the email included in the parameters
            cursor.execute(updateQuery, (firstname, lastname, password, country, phone, dob, role, email))
            connection.commit()
            flash("Your details have been updated successfully.", "success")
        except Exception as e:
            flash(f"An error occurred while updating details: {e}", "error")
        finally:
            cursor.close()
            connection.close()
    else:
        flash("Failed to connect to the database", "error")

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()  # Clear the session data
    flash("Successfully logged out", "success")  # Flash a success message
    return redirect(url_for("home"))  # Redirect to the home page after logout


@app.route("/close_account", methods=["POST"])
def close_account():
    # Ensure the user is logged in
    if 'user_email' not in session:
        return redirect('/login')

    # Check if the user confirmed by typing "CLOSE"
    confirmation = request.form.get("confirm")

    if confirmation != "CLOSE":
        #flash("Account closure was not confirmed. Please type 'CLOSE' to confirm.", "error")
        return render_template("close_account.html")

    # If the confirmation is correct, proceed to delete the account
    try:
        user_email = session['user_email']
        connection = create_connection()

        if connection:
            cursor = connection.cursor()

            # Query to delete the user from the database
            delete_user_query = "DELETE FROM users WHERE email = %s"
            cursor.execute(delete_user_query, (user_email,))
            connection.commit()

            # Log the user out and flash a success message
            #session.pop('user_email', None)
            flash("Your account has been closed and all your data has been deleted.", "success")

            # Close the database connection
            cursor.close()
            connection.close()
        else:
            flash("Failed to connect to the database. Please try again later.", "error")
    except Exception as e:
        flash("An error occurred while closing your account. Please try again later.", "error")

    # Redirect to the home page after the operation
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
