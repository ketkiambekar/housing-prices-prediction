from flask import Flask, render_template, jsonify,request
import joblib
import os

app = Flask(__name__)
#app.config["DEBUG"]=True

print(os.getcwd())
my_model= joblib.load("model/HousingPrices")

@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/result', methods=['POST'])
def predict():
    try:
        bedrooms =  int(request.form.get("bedrooms"))
        bathrooms =  int(request.form.get("bathrooms"))
        sqft_living =  int(request.form.get("sqft_living"))
        grade =  int(request.form.get("grade"))
        view =  int(request.form.get("view"))
        feed = [[bedrooms, bathrooms, sqft_living, grade, view]]
        price = my_model.predict(feed)
        return  render_template('/index.html',message="Predicted Price: ${:,.2f}".format(price[0]))
    except Exception as e:
        return render_template('/index.html', message="Error: "+str(e) )
 
if __name__ == '__main__':
   app.run()