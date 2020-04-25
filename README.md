# Docker micropython

Docker image that setups a micropython container that executes a boot script at startup.

To launch several instances run (**STILL NOT TESTED**): 

`docker-compose up -d --scale micropython_docker=5`