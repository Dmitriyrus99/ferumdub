FROM python:3.10-slim

RUN apt-get update && apt-get install -y git mariadb-client redis-server nodejs npm yarn curl

WORKDIR /home/frappe

# Add frappe user and group / nege esnsovan maten
exec getent group frappe || addgroup frappe && echo "group added || exit 0" && exec id -u frappe || adduser --disabled-password --gecos "" frappe && usermod -aG
frappe frappe

USER frappe

RUN mkdir -p /home/frappe
WORKDIR /home/frappe
WORKDIR /home/frappe/frappe-bench
RUN chown -R frappe /home/frappe

RUN bench init frappe-bench --frappe-branch version-15
