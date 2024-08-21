# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import logging

app = Flask(__name__)  # initializing a Flask app

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            research = 1 if is_research == 'yes' else 0

            # Loading the model file from the storage
            filename = 'finalized_model.pickle'
            with open(filename, 'rb') as file:
                loaded_model = pickle.load(file)

            # Predictions using the loaded model file
            prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
            logging.debug(f'Prediction: {prediction}')

            # Showing the prediction results in a UI
            return render_template('results.html', prediction=round(100 * prediction[0]))

        except Exception as e:
            logging.error(f'Exception: {e}')
            return 'Something went wrong. Please check your inputs and try again.'

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)  # Running the app
