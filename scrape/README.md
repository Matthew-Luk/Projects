## Docker
* Install [docker](https://www.docker.com/) for PC.
* Start docker daemon on your PC.
* Run `docker-compose build` to build `docker-compose.yml` file.
* Run `docker-compose up` to create the infrastructure in `docker-compose.yml`.
* `CTRL+C` to terminate allocated infrastructure and `docker-compose down -v` to delete App. 
  
## Testing
* `pip install -U pytest`
* Run command `pytest` in parent directory