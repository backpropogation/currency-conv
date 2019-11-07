#!/bin/sh

echo "migrate"
docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py migrate