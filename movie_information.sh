#!/usr/bin/bash

image_name="alabaster:1.0"

docker run -v "${PWD}":/usr/src/app:ro "${image_name}" movie_information.py $@

