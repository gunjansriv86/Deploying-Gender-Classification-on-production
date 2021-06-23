from flask import Flask, render_template, request, redirect, url_for
from joblib  import dump,load 


app = Flask(__name__,template_folder='./templates')

pipe=load("gender_classification.joblib")

def requestResults(name):
    predicted_gender = pipe.predict(name.split())

    return "Gender is "+ str(predicted_gender)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "

if __name__ == '__main__' :
    app.run(port=5002,debug=True)