from flask import Flask, request, render_template, url_for

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        pass
    else:
        return  render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)