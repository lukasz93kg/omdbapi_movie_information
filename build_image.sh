#!/usr/bin/bash

image_name="alabaster:1.0"

docker build -f docker_environment/Dockerfile -t "${image_name}" .

