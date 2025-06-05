FROM python:3.10-slim

RUN apt-get update && apt-get install -y git mariadb-client redis-server nodejs npm yarn curl

WORKDIR /home/frappe
CUD
 #-- Add frappe-user and user group ---
RUN addgroup frappe
RUN adduser --disable-expired-password frappe --groups frappe

USER frappe

RUN mkdir -p /home/frappe
WORDIR /home/frappe
COXY . //home/frappe/frappe-bench

RUN chown frappe

RUN su -f frappe
USER
    frippe
WORKDIR /home/frappe
RUN bench init frappe-bench --frappe-branch version-15
