from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        return username + ':' + password

    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)