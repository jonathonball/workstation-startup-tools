# Docker Quick Reference

## Run an interactive bash session in a new container
`docker run -it --entrypoint /bin/bash centos:7`

## View containers
`docker container ls --all`

## Run an interactive bash session in a running container
`docker exec -it [CONTAINER_HASH] /bash/bash`

