#FILENAME = 'movies.txt'
FILENAME = 'dmd.in'

def write_movies(movies):
    with open(FILENAME, 'w') as file:
        for movie in movies:
            file.write(movie + '\n')


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace('\n', '')
            movies.append(line)
    return movies


def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + '. ' + movie)
    print()


def add_movie(movies):
    movie = input('Movie: ')
    movies.append(movie)
    write_movies(movies)
    print(movie + ' was added.\n')


def delete_movie(movies):
    index = int(input('Number: '))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + ' was deleted.\n')


def display_menu():
    print("The Movie List program")
    print()
    print('COMMAND MENU')
    print('list - List all movies')
    print('add - Add a movie')
    print('del - Delete a movie')
    print('exit - Exit program')
    print()
