class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies

class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Драмы: {self.movies}"


comedy_mov = Comedy()
drama_mov = Drama()
result_comedy = comedy_mov.add_movie('Большой куш')
result_drama = drama_mov.add_movie('Оружейный барон')

print(result_comedy)
print(result_drama)