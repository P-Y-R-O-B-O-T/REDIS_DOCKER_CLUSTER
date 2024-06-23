import sys
from jinja2 import Environment, FileSystemLoader

#######################
# DOCKER COMPOSE FILE #
#######################

REDIS_CLUSTER_PORT = 9000
REDIS_NGINX_LISTEN_PORT = 6379
NODES = int(sys.argv[1])

ENVIRONMENT = Environment(loader=FileSystemLoader("./templates/"))
COMPOSE_TEMPLATE = ENVIRONMENT.get_template("compose_template.yaml")
NGINX_TEMPLATE = ENVIRONMENT.get_template("nginx_template.conf")

content = COMPOSE_TEMPLATE.render(number_nodes=NODES)

with open("compose.yaml", "w") as compose_file :
    compose_file.write(content)

content = NGINX_TEMPLATE.render(number_nodes=NODES,
                                redis_cluster_port=REDIS_CLUSTER_PORT,
                                redis_nginx_listen_port=REDIS_NGINX_LISTEN_PORT)

with open("nginx/nginx.conf", "w") as nginx_config_file:
    nginx_config_file.write(content)
