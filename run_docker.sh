#!/bin/bash

docker build -t scrape:latest .

docker run -it -v /home/cosmos/Desktop/serenay/my_new_docker_build:/serenay scrape