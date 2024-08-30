from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/via_postman', methods=['POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':
        try:
            data = request.json  # Access JSON data from request body
            operation = data['operation']
            num1 = int(data['num1'])
            num2 = int(data['num2'])
        except KeyError as e:
            return jsonify({"error": f"Missing key: {e.args[0]}"})
        except ValueError as e:
            return jsonify({"error": "Invalid input, please provide numerical values for num1 and num2"})

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return jsonify({"error": "Unsupported operation"})

        return jsonify({"result": result})


@app.route("/vithu", methods = ["GET", "POST"])
def math_vithu():
    if request.method == "POST":
        num0 = int(request.json["num0"])
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        result = num0 * num1 * num2
        return  jsonify(result)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]

        if username == "Admin" and password == "1234":
            return jsonify("login success")
        else:
            return jsonify("login failed")

if __name__ == '__main__':
    app.run(debug=True)
