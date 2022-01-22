# omdbapi movie information

The mini project for checking the rating of a movie :)

Script printing Rotten Tomatoes rating and movie title


# General information/Limitation
  1. Script using APIKEY which can be used 1000 times per day
     Remember that APIKEY is hardcoded and can be shared whith all whom are using this application

     Recommendation: You can generate your own APIKEY on http://omdbapi.com/apikey.aspx  and use it from parameter or hardcode in modules/omdbapi.py

# REQUIREMENTS:
  1. Installed docker
     Script was tested on: Docker version 20.10.7, build 20.10.7-0ubuntu5~21.04.2
  2. Permission to running docker containers on machine

# Building and running the application
  1. Build docker image:
     - run script build_image.sh:
       ./build_image.sh
  2. run application - run bash scripts with parameters (script passing all parameters into a movie_information.py script) this script helping us to run all things without running docker commends, but you can also do the clean run using docker
     ex. ./movie_information.sh <movie_name> [--apikey APIKEY]
    ./movie_information.sh mask
    ./movie_information.sh -h
    ./movie_information.sh Avengers --apikey "513d7fc9"

