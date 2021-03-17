#!/bin/bash

docker build -t text-ide -f ./Dockerfile .

docker run --net=host -e DISPLAY=:0 text-ide

#docker run -ti --net=host -e DISPLAY=:0 text-ide

#docker run --rm --name text-ide text-ide

#glibc

#docker run text-ide --privileged

#docker run text-ide --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" text-ide

#docker run --name text-IDE text-IDE
