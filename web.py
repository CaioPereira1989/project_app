# Caio Pereira and Jingjing Yao
#Web.py file for final project 

from flask import Flask, render_template
import giphypop
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
	gif_search = request.values.get('search_words')
	g = giphypop.Giphy()
	if gif_search == "";
		return render_template('index.html')
	else:
		results = g.search(gif_search)
	

	return render_template('results.html')


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
#app.run(debug=True)