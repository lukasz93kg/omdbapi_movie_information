import requests
import ast
from typing import Any, List

class Omdbapi():
    def __init__(self, movie_name: str, omdb_apikey: str="513d7fc9") -> None:
        self.movie_name = movie_name
        self.apikey = omdb_apikey
        self.omidb_url = "http://www.omdbapi.com"
        self.movie_data = self.__get_movie_information_from_omdbapi()
        self.__key_value_print_format = "{:25} {}"

    def __get_movie_information_from_omdbapi(self) -> dict:
        '''
        Return full movie information

            Returns:
                movie_information (dict): All movie information structure
        '''
        get_movie_information = requests.get("{}/?t={}&apikey={}".format(self.omidb_url, self.movie_name, self.apikey))
        get_movie_information.raise_for_status()
        # bytes type to python readable structure
        movie_information = ast.literal_eval(get_movie_information.content.decode("utf-8"))
        if "Error" in movie_information:
            raise Exception("Movie \"{}\" not found. Returned value from {} is {}.".format(self.movie_name, self.omidb_url, movie_information))
        return movie_information
    
    def get_video_property(self, property_name: str="Title") -> Any:
        '''
        Return value for given property name

            Parameters:
                property_name (str): Name of property which We would like to gather (default: Title)

            Returns:
                property_value (Any): Value of provided property
        '''
        property_value = self.movie_data[property_name]
        return property_value

    def get_ratings_property(self, rating_names: List[str]=["Rotten Tomatoes"], ratings_property_name: str="Ratings") -> dict:
        '''
        Return rating name and rating value

            Parameters:
                rating_names (List[str]): Name of choosen ex. (Internet Movie Database, Metacritic) rating from omdbapi (default: Rotten Tomatoes)
                rating_property_name (str): Name of field from the omdbapi output where ratings are now (prepared if name will be changed)
            
            Returns:
                rating_properties (dict): Dictionary of rating name and rating values
        '''
        ratings_property_list = self.get_video_property(ratings_property_name)
        rating_properties = dict()
        for rating_property in ratings_property_list:
            if rating_property['Source'] in rating_names:
                rating_properties[rating_property["Source"]] = rating_property["Value"]
        if not rating_properties:
            print("No values was found for rating names {}".format(rating_names))
        return rating_properties

    def _print_rating_information(self, *rating_names: List[str]) -> None:
        '''
        Function for printing rating information

            Parameters:
                rating_names - This parameter working only for property name Ratings
                rating_names (List[str]): Name of choosen ex. (Internet Movie Database, Metacritic) rating from omdbapi (default: Rotten Tomatoes)
        '''
        if rating_names:
            rating_properties = self.get_ratings_property([*rating_names])
        else:
            rating_properties = self.get_ratings_property()
        for rating_name, rating_value in rating_properties.items():
            print(self.__key_value_print_format.format(rating_name, rating_value))
 
    def _print_property(self, property_name) -> None:
        '''
        Function for printing choosen property
        For more pretty way of printing "Ratings" field you can use method _print_rating_information

            Parameters:
                property_name (str): Name of property which We would like to gather (default: Title)

        '''
        movie_property_value = self.get_video_property(property_name)
        print(self.__key_value_print_format.format(property_name, movie_property_value))

    def print_property(self, property_name: str, *rating_names: List[str]) -> None:
        '''
        Function for printing choosen movie information

            Parameters:
                property_name (str): Name of property which We would like to gather (default: Title)
                rating_names - This parameter working only for property_name="Ratings"
                rating_names (List[str]): Name of choosen ex. (Internet Movie Database, Metacritic) rating from omdbapi (default: Rotten Tomatoes)
        '''
        if property_name == "Ratings":
            if rating_names:
                self._print_rating_information(*rating_names)
            else:
                self._print_rating_information()
        else:
            self._print_property(property_name)
    
    def __str__(self) -> None:
        '''
        Printing all movie information for an Omdbapi object
        '''
        print_object = ""
        for property_name, property_value in self.movie_data.items():
            print_object = print_object + self.__key_value_print_format.format(property_name, property_value)
        return print_object


if __name__ == "__main__":
    my_movie = Omdbapi("Mask")

    my_movie.print_property("Title")
    my_movie.print_property("Ratings", "Internet Movie Database", "Rotten Tomatoes")
    print(my_movie)