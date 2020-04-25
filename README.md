# Docker micropython

Docker image that setups a micropython container that executes a boot script at startup.


## Commands 

To launch several instances run (**STILL NOT TESTED**): 

`docker-compose up -d --scale micropython_docker=5`

Get ip addresses of container:

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker-micropython_micropython_1`


### Aux commands

Remove all images:

`docker rmi $(docker images -a -q)`

Prune: 

`docker system prune`