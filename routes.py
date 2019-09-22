import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
	if request.method=='POST':

		entered_li = []


		# ---YOUR CODE FOR Part 2.2.3 ----  

		# Define "day", "open", "prn", "state", "school", and "store" variables

		day_of_week = request.form['day_of_week']
		store_open = request.form['open']
		promo = request.form['promo']
		state_holiday = request.form['state_holiday']
		school_holiday = request.form['school_holiday']
		promo2 = request.form['promo2']
		
		# convert a,b,c,d to 1,2,3,4 for store_type and assortment

		store_type = ord(request.form['store_type']) - 96
		assortment = ord(request.form['assortment']) - 96


		# --- THE END OF CODE FOR Part 2.2.3 --- 

		# StoreType, Assortment, CompetitionDistance... arbitrary values

		competition_distance = 290.0
		competition_open_since_month = 10.0
		competition_open_since_year = 2011.0
		competition_open_since_month_missing = 0.0
		competition_open_since_year_missing = 0.0	
		competition_distance_missing = 0.0

		if promo2 == 1: 
			promo2_since_week = 40.0
			promo2_since_year = 2014.0
		else:
			promo2_since_week = 0.0
			promo2_since_year = 0.0

		for val in [day_of_week, 
					store_open, 
					promo, 
					state_holiday, 
					school_holiday, 
					store_type, 
					assortment, 
					competition_distance, 
					competition_open_since_month, 
					competition_open_since_year, 
					promo2, 
					promo2_since_week, 
					promo2_since_year, 
					competition_open_since_month_missing, 
					competition_open_since_year_missing, 
					competition_distance_missing]:
			entered_li.append(val)

		# for val in [1, 1, 290.0, 10.0, 2011.0, 1, 40.0, 2014.0, 0, 0, 0]:
			# entered_li.append(val)


		# ---YOUR CODE FOR Part 2.2.4 ---- 
		
		# Predict from the model

		prediction = model.predict(np.array(entered_li).reshape(1, -1))



		# --- THE END OF CODE FOR Part 2.2.4 --- 
		
		label = str(np.squeeze(prediction).round(2))

		return render_template('index.html', label=label)


if __name__ == '__main__':

	# ---YOUR CODE FOR Part 2.2.1 ----  
	
	#Load ML model

	model = joblib.load('rm.pkl')




	# --- THE END OF CODE FOR Part 2.2.1 --- 

	# start API
	app.run(host='0.0.0.0', port=8000, debug=True)


