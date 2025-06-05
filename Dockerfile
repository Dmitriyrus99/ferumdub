FROM python:3.10-slim

RUN apt-get update && apt-get install -y git mariadb-client redis-server nodejs npm yarn curl

WORKDIR /home/frappe/frappe-bench

RUN addgroup frappe && adduser --disabled-password --gecos "" --ingroup frappe frappe

USER frappe

RUN mkdir -p /home/frappe && cd /home/frappe && pip install frappe-bench && bench init frappe-bench --frappe-branch version-15

WORKDRHD/home/frappe/frappe-bench

RUN chown -R frappe /home/frappe
