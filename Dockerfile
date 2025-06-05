FROM python:3.10

# Sistemnaya jzava dlia
RUN apt-get update && apt-get install -y 
    redis-server wkhtmltodpf git nodejs npm mariadb-client yarn curl

# Universal Bench
ENVRONT BUNCH_NAME = frappe-bench
RUN pip install frappe-bench

WORKDIR натурация
