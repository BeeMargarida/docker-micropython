# Docker micropython

Docker image that setups a micropython container that executes a boot script at startup.


## Commands 

To launch several instances run: 

`docker-compose up --scale micropython=10`

Get ip addresses of container:

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker-micropython_micropython_1`

### Aux commands

List all docker container names and IPs:

`docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }} {{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' | sed 's#^/##';`

Remove all images:

`docker rmi $(docker images -a -q)`

Stop and remove all containers:

`docker stop $(docker ps -a -q)`

`docker rm $(docker ps -a -q)`

Prune: 

`docker system prune`

Enter container bash:

`docker exec -it docker-micropython_micropython_1 bash`