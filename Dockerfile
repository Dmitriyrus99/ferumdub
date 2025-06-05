FROM python:3.10-slim

RUN apt-get update && apt-get install -y git mariadb-client redis-server nodejs npm curl cron && npm install -g yarnt=1.22.19

USER frappe
WORKDIR /home/frappe

RUN pip install --user frappe-bench && \
    ~/.local/bin/bench init frappe-bench --frappe-branch version-15 --skip-assets

COPY bootstrap.sh /bootstrap.sh
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT "/entrypoint.sh"