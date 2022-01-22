#!/usr/bin/bash

image_name="alabaster:1.0"
pushd docker_environment
  docker build -t "${image_name}" .
popd

