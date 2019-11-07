README
=====================

This readme descripes all steps for starting web app.

##### SETUP  BACKEND

* [INSTALL DOCKER](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* `sudo groupadd docker`
* `sudo gpasswd -a ${USER} docker`
* `newgrp docker`
* `sudo service docker restart`
* [Install docker-compose](https://docs.docker.com/compose/install/)
* `sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`
* `docker-compose build`
* `chmod +x start.sh`
* `./start.sh`
* wait untill ALL containers are up
* `chmod +x migrate.sh`
* `./migrate.sh`
##### SETUP FRONTEND 
* `sudo apt-get install npm`
* `sudo npm install`
* `sudo npm run start`
##### Frontend address 
* http://localhost:3000/

##### Backend address 
* http://0:0:0:0:8000
