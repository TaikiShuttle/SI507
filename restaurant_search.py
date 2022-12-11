from flask import Flask
from flask import render_template
import constructTree
from flask import request
import math

app = Flask(__name__)

# construct the tree, this is a tree contains all the restaurants
kdtree = constructTree.constructTree()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/restaurant_map')
def restaurants():
    return render_template('restaurant_map.html')

@app.route('/single_search', methods=['POST', 'GET'])
def single_search():
    results = None
    if request.method == 'POST':

        # get the search parameters
        how = request.form['how']
        if how == 'name':
            query = request.form['search']
        else:
            query = float(request.form['search'])

        # get the result
        results = kdtree.single_search(node = kdtree.root, query = query, how = how)

        # modify the price to be None if the price is inf
        for result in results:
            if result.price == float('inf'):
                result.price = None

        if not results:
            results = []
    
    return render_template('single_search.html', results = results)

@app.route('/range_search', methods = ['POST', 'GET'])
def range_search():
    results = None
    if request.method == 'POST':

        # get the search parameters
        # ranges: the range to search [minPopulation, maxPopulation, minRating, maxRating, minPrice, maxPrice, minName, maxName]
        minPopulation = float(request.form['minPopulation']) if request.form['minPopulation'] else 0
        maxPopulation = float(request.form['maxPopulation']) if request.form['maxPopulation'] else math.inf
        minRating = float(request.form['minRating']) if request.form['minRating'] else 0
        maxRating = float(request.form['maxRating']) if request.form['maxRating'] else 5
        minPrice = float(request.form['minPrice']) if request.form['minPrice'] else 0
        maxPrice = float(request.form['maxPrice']) if request.form['maxPrice'] else math.inf
        minName = request.form['minName'] if request.form['minName'] else 'A'
        maxName = request.form['maxName'] if request.form['maxName'] else 'z'

        # get the result
        results = kdtree.rangeSearch(node = kdtree.root, ranges = [minPopulation, maxPopulation, minRating, maxRating, minPrice, maxPrice, minName, maxName], depth = 0)

        # modify the price to be None if the price is inf
        for result in results:
            if result.price == float('inf'):
                result.price = None

        if not results:
            results = []        

    return render_template('range_search.html', results = results)

@app.route('/relations')
def relations():
    return render_template('relations.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(ssl_context=('cert.pem', 'key.pem'))