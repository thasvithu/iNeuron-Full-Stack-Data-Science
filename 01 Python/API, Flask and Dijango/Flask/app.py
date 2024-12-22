from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Debug: Print the form data to the console
        print(request.form)

        try:
            name = request.form['name']  # Get the value of the 'name' field
            return f"Hello {name}!"  # Return a greeting with the entered name
        except KeyError:
            return "Name field is missing in the form!"  # Error handling if 'name' is not found in form data

    return render_template("form.html")  # Render the form on GET request


if __name__ == "__main__":
    app.run(debug=True)
