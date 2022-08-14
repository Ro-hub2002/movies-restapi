from flask import Flask, jsonify, request

app = Flask(__name__)

from movies import movies

@app.route('/probando')
def ping():
    return jsonify({"message": "Welcome to my API"})

@app.route('/movies')
def getMovies():
    return jsonify({"movies": movies, "message": "Movies List"})

@app.route('/movies/<string:movie_name>')
def getMovie(movie_name):
    moviesFound = [movie for movie in movies if movie['name'] == movie_name]
    if (len(moviesFound) > 0):
        return jsonify({"movies": moviesFound[0]})
    return jsonify({"message": "No movies found"})

@app.route('/movies', methods=['POST'])
def addMovie():
    new_movie = {
        "name": request.json['name'],
        "price": request.json['price'],
        "ticket": request.json['ticket']
    }
    movies.append(new_movie)
    return jsonify({'message': "Movie added successfully", "movies": movies})

@app.route('/movies/<string:movie_name>', methods=['PUT'])
def updateMovie(movie_name):
    movieFound = [movie for movie in movies if movie['name'] == movie_name]
    if (len(movieFound) > 0):
        movieFound[0]['name'] == request.json['name']
        movieFound[0]['price'] = request.json['price']
        movieFound[0]['ticket'] = request.json['ticket']
        return jsonify({'message': "Movie updated successfully", "movie": movieFound})
    return jsonify({"message": "Product not found"})

@app.route('/movies/<string:movie_name>', methods=['DELETE'])
def deleteMovie(movie_name):
    moviesFound = [movie for movie in movies if movie['name'] == movie_name]
    if (len(moviesFound) > 0):
        movies.remove(moviesFound[0])
        return jsonify({'message': "Movie deleted successfully", "movies": movies})
    return jsonify({'message': "Movie not found"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)




