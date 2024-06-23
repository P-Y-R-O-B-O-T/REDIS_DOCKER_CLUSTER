# REDIS_MINE

![](ZZZ/ZZZ.jpg) 

This project provides a solution to deploy, configure, and maintain a highly available Redis cluster on Docker Swarm. It includes features for dynamic scaling and load balancing using NGINX as a reverse proxy. Configuration files are dynamically generated using Jinja templating for greater flexibility and ease of management.

## Features
* **Highly Available Redis Cluster**: Deploy a Redis cluster with multiple nodes to ensure high availability and fault tolerance.
* **Dynamic Scaling**: Generate configuration and cpoy to scale the Redis cluster based on demand.
* **Load Balancing**: Use NGINX as a reverse proxy to distribute traffic evenly across Redis nodes.
* **Docker Swarm Integration**: Leverage Docker Swarm for orchestration and management of the Redis cluster.
* **Jinja Templating**: Generate configuration files dynamically using Jinja templates.

## Prerequisites
* Docker
* Docker Swarm initialized
* Docker Compose (optional for easier configuration)
* Python (for Jinja templating)

## Architecture
* **Redis Cluster**: Consists of master and slave nodes to ensure data redundancy and high availability.
* **NGINX**: Acts as a reverse proxy to distribute incoming traffic to the Redis nodes.
* **Docker Swarm**: Manages the deployment, scaling, and orchestration of the services.
* **Jinja Templating**: Used to dynamically generate configuration files.

## INSTALL DEPENDENCIES
* `pip install Jinja2`
* Install docker engine based on your linux distro

## USAGE
* Clone the repository
```
git clone https://github.com/P-Y-R-O-B-O-T/REDIS_DOCKER_CLUSTER.git
```
* Change into the repository directory
* Change the templates for redis, nginx, yaml config and all the Dockerfiles for redis and nginx according to requirements
* Generate the configuration with `N` redis nodes
```
python3 gen_config.py N
```
* Now all the configurations are available at `compose.yaml`, `redis/redis.conf` and `nginx/nginx.conf`
* Build the docker images
```
cd redis
sudo docker build -t redis_mine .
cd ../nginx
sudo docker build -t nginx_redis_mine .
```
* Kill existing docker containers, or do manually select the containers that belong to this project yourself
```
sudo docker container rm $(sudo docker container ls -qa)
```
* Remove all the docker volumes if no important data present in them or manually delete the volumes that are associated with this project or are having label
```
sudo docker volume rm $(sudo docker containers ls -aq)
```
* Test the configuration: goto root directory of this project and run the following command
```
sudo docker compose up
```
* Now we can connect to the cluster using the `resis-cli` tool by specifying `PORT`, port is the port that is used in the nginx configuration to listen to
```
redis-cli -c -h HOST_IP_NAME -p PORT
```
## DEPLOYMENT
* Once the configuration is verified, we must push the images to the local registry
* Copy the contents of `compose.yaml` into your project's yaml configuration and the update the cluster
