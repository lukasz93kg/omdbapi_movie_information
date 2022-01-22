import requests
import json
from typing import List

#x = requests.get('http://www.omdbapi.com/?t=mask&apikey=513d7fc9')
#data = x.json()



#print(x.content)
#print(data)

#y = b'{"Title":"Mask","Year":"1985","Rated":"PG-13","Released":"22 Mar 1985","Runtime":"120 min","Genre":"Biography, Drama","Director":"Peter Bogdanovich","Writer":"Anna Hamilton Phelan","Actors":"Cher, Eric Stoltz, Sam Elliott","Plot":"A teenager with a massive facial skull deformity and biker gang mother attempt to live as normal a life as possible under the circumstances.","Language":"English","Country":"United States","Awards":"Won 1 Oscar. 3 wins & 7 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BYTVlYjExOWEtZmU5Yy00N2VjLWJmY2UtZjZiYzMzYzhhYjNiXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.2/10"},{"Source":"Rotten Tomatoes","Value":"93%"},{"Source":"Metacritic","Value":"73/100"}],"Metascore":"73","imdbRating":"7.2","imdbVotes":"28,144","imdbID":"tt0089560","Type":"movie","DVD":"22 Aug 1997","BoxOffice":"$48,230,162","Production":"N/A","Website":"N/A","Response":"True"}'
#y = y.json()
json_y = '''
{
    'Title': 'Mask', 
    'Year': '1985',
    'Rated': 'PG-13',
    'Released': '22 Mar 1985',
    'Runtime': '120 min',
    'Genre': 'Biography, Drama',
    'Director': 'Peter Bogdanovich',
    'Writer': 'Anna Hamilton Phelan',
    'Actors': 'Cher,Eric Stoltz, Sam Elliott',
    'Plot': 'A teenager with a massive facial skull deformity and biker gang mother attempt to live as normal a life as possible under the circumstances.',
    'Language': 'English',
    'Country': 'United States',
    'Awards': 'Won 1 Oscar. 3 wins & 7 nominations total',
    'Poster': 'https://m.media-amazon.com/images/M/MV5BYTVlYjExOWEtZmU5Yy00N2VjLWJmY2UtZjZiYzMzYzhhYjNiXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_SX300.jpg',
    'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.2/10'}, {'Source': 'Rotten Tomatoes', 'Value': '93%'}, {'Source': 'Metacritic', 'Value': '73/100'}],
    'Metascore': '73',
    'imdbRating': '7.2',
    'imdbVotes': '28,144',
    'imdbID': 'tt0089560',
    'Type': 'movie',
    'DVD': '22 Aug 1997',
    'BoxOffice': '$48,230,162',
    'Production': 'N/A',
    'Website': 'N/A',
    'Response': 'True'
}
'''

import ast
movie_information = ast.literal_eval(json_y)


def get_video_property(property_name: str="Title"):
    return movie_information[property_name]

def get_ratings_property(rating_names: List[str]=["Rotten Tomatoes"], ratings_property_name: str="Ratings"):
    ratings_property_list = get_video_property(ratings_property_name)
    rating_properties = dict()
    for rating_property in ratings_property_list:
        if rating_property['Source'] in rating_names:
            rating_properties[rating_property["Source"]] = rating_property["Value"]
    if not rating_properties:
        print("Any of following properties was not found for rating names {}".format(rating_names))
    return rating_properties


print(get_video_property())
rating_properties=get_ratings_property(['Internet Movie Database', "Rotten Tomatoes"])

for rating_name, rating_value in rating_properties.items():
    print("{} {}".format(rating_name, rating_value))