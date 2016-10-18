# Caio Pereira and Jingjing Yao
#Web.py file for final project 

#YOU WILL FIND COMMMENTS IN THIS FILE AND ALSO IN THE .HTML FILES
# Import the necessary libraries, functions and classes
from flask import Flask, render_template, request
import giphypop
import os
app = Flask(__name__)



#Page 1: User can perform a search of any GIF

@app.route('/')
def index():
	return render_template('index.html')

#Page 2: About the authors (Caio Pereira and Jingjing Yao)

@app.route('/about')
def about():
	return render_template('about.html')

#Page 3: Display the results of the search

@app.route('/results')
def results():
	gif_search = request.values.get('search_words') #uses the function from "request"
	g = giphypop.Giphy()
	if gif_search == "": 							#if the search is blank, return homepage
		return render_template('index.html')
	else:
		results = g.search(gif_search) 	 			#uses function g.search from giphypop
		#line below: passes results and gif_search to html
		return render_template('results.html', results=results, gif_search=gif_search)

#extracted from canvas
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
