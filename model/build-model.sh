#!/bin/sh
# Use dockerfile to build model.pt
# First start by building container
echo $(pwd)
docker build . -t build-t5-model:1.0 -f Dockerfile.build
docker run --gpus all --rm -v $(pwd):/app build-t5-model:1.0
