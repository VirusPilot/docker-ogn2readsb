### docker version of https://github.com/b3nn0/ogn2dump1090
![ogn2readsb](https://github.com/user-attachments/assets/0e3c71e2-113a-4b45-88c6-007bedd7a064)
### supported operating systems
Debian-based Linux Operating Systems (64bit Bookworm or newer)
- Ubuntu
- DietPi
- RaspiOS

### supported hardware architectures
- arm64 (64-bit ARM CPUs with hardware floating point processor)
- x64 (64-bit AMD/Intel CPUs)

### prepare
- identify both SDR serials (e.g. 868 and 1090), they are required for the `config.vars` below
- `sudo apt update && sudo apt install git`
- `git clone https://github.com/VirusPilot/docker-ogn2readsb`
- `cd docker-ogn2readsb`
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo usermod -aG docker $USER && newgrp docker`

### configuration
- `cd ./docker-ogn2readsb`
- `nano config.vars`
  - save changes with `CTRL O`
  - exit nano with `CTRL X`

| variable | example | description |
| :--- | :--- | :--- |
| STATION_LAT | 50.0 | your station latitude [deg] (as positive or negative decimal number)|
| STATION_LON | 10.0 | your station longitude [deg] (as positive or negative decimal number)|
| STATION_ALT_MSL_M | 300 | your station altitude AMSL [m] |
| STATION_NAME | OGNTEST | your max. 9 letter station name, please comply with [naming convention](http://wiki.glidernet.org/receiver-naming-convention) |
| FREQ_PLAN | 1 | 1=EU/Africa (default), 2=USA/Canada, 3=South America/Australia, 4=New Zeeland, 5=Israel, 6=EU/Africa 433MHz |
| GSM_CENTER_FREQ | 935.8 | default = 0, change only if you know your closest GSM900 station frequency [MHz] |
| ADSB_MAX_ALT_FT | 18000 | ADSB max OGN feed altitude [ft] |
| METAR_SOURCE_ICAO | EDDF | 4 letter ICAO code of a nearby airport with [METAR](https://aviationweather.gov) service |
| APRS_SUBSCRIBE_FILTER | r/50.0/10.0/100 | circle in [km] around a defined postion (example: LAT 50.0, LON 10.0, CIRCLE 100 km) for which you want to receive traffic from the OGN APRS servers |
| SDR_868_SERIAL | 868 | enter your OGN SDR serial |
| SDR_868_PPM | 0 | change only if you know your SDR's ppm |
| SDR_1090_SERIAL | 1090 | enter your ADSB SDR serial |
| SDR_1090_PPM | 0 | change only if you know your SDR's ppm |

### build
- `docker compose up --detach --build`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

### apply configuration changes
- `cd ./docker-ogn2readsb`
- `nano config.vars`
- `docker compose up --detach --build`

### monitor all ADSB and OGN traffic consolidated in a single tar1090 instance
- `http://yourRaspberryPi.local/tar1090`

### monitor OGN details
- `http://yourRaspberryPi.local:8080`
- `http://yourRaspberryPi.local:8081`

### monitor docker containers
- `docker logs -f rtlsdr-ogn`
- `docker logs -f mlat-client-adsbx`
- `docker logs -f readsb`
- `docker logs -f ogn2dump1090`
- `docker logs -f tar1090`

### useful docker commands
- `docker ps -a` list all docker containers, including stopped ones
- `docker stop <container_name_or_id>` stop a running container
- `docker rm <container_name_or_id>` deactivate a stopped container
- `docker container prune` deactivate all stopped containers
- `docker image ls` list docker images
- `docker rmi <image_id_or_name>` delete docker image
- `docker image prune` delete all docker images
- `docker system prune -a --volumes` clean your docker environment
