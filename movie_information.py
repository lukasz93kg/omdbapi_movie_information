from modules.omdbapi import Omdbapi
import argparse

def read_program_parameters():
    parser = argparse.ArgumentParser(description="Script for taking movie information")
    parser.add_argument("movie_name", type=str, help="Name of movie for which you would like to gather information")
    parser.add_argument("-i", "--apikey", type=str, help="Api key for connection to the http://omdbapi.com/. Default is hardcoded")
    return parser.parse_args()


def main():
    program_arguments = read_program_parameters()
    movie_name = program_arguments.movie_name
    omdb_apikey = program_arguments.apikey
    if omdb_apikey:
        my_movie = Omdbapi(movie_name, omdb_apikey)
    else:
        my_movie = Omdbapi(movie_name)
    my_movie.print_property("Title")
    my_movie.print_property("Ratings", "Internet Movie Database", "Rotten Tomatoes")
    my_movie._print_property("Ratings")


main()