FROM python:3.10-slim

RUN apt-get update && apt-get install -y git mariadb-client redis-server nodejs npm yarn curl

WORKDIR /frappe-bench

RUN pip install frappe-bench
RUN bench init frappe-bench --frappe-branch version-15
WORKDIR /frappe-bench

COPY . /frappe-bench/apps/ferum_customs
RUN bench get-app ferum_customs
rUN bench new-site your-site-name
RUN bench --site your-site-name install-app ferum_customs