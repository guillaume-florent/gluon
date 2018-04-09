#!/usr/bin/env bash

xhost +local:gluon
docker start gluon
docker exec -it gluon /bin/bash