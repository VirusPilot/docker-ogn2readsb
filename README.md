### docker version of [ogn2readsb](https://github.com/b3nn0/ogn2dump1090)
![ogn2readsb](https://github.com/user-attachments/assets/0e3c71e2-113a-4b45-88c6-007bedd7a064)
### supported operating systems
Debian or Debian-based Linux Operating Systems (64bit Bookworm or newer):
- Debian
- Ubuntu
- DietPi
- RaspiOS

### supported hardware architectures
- arm64 (64-bit ARM CPUs with hardware floating point processor)
- x64 (64-bit AMD/Intel CPUs)

### prepare system
- `sudo apt update && sudo apt install git`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`

### prepare docker
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo usermod -aG docker $USER && newgrp docker`

### prepare SDRs
- identify or set both SDR serials (e.g. 868 and 1090), they are required for the `config.vars` below
- unplug all SDRs, leaving only the SDR to be used for 1090 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_eeprom ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -s 1090`
- unplug all SDRs, leaving only the SDR to be used for 868 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_eeprom ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -s 868` 

### prepare ogn2readsb
- `git clone https://github.com/VirusPilot/docker-ogn2readsb`

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

### option to merge inconsistent address type transmissions
- `cd ./docker-ogn2readsb`
- `nano tar1090/Dockerfile`
-  add ` && echo 'MergeNonIcao = true;' >> config.js` after `echo 'jaeroLabel = "OGN";' >> config.js`

### build (without multiple feeders)
- `cd ./docker-ogn2readsb`
- `docker compose up --detach --build`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

### ADVANCED build (with multiple feeders included)
- `cd ./docker-ogn2readsb`
- `nano compose-multifeed.yaml`
  - add your feeder credentials (e.g. SHARING KEY, USERNAME, LAT, LON, ALT)
  - delete (or comment out) unused/unwanted feeder entries
- `docker compose --file compose-multifeed.yaml up --detach --build`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

### apply configuration changes
- `cd ./docker-ogn2readsb`
- `nano config.vars`
- `docker compose up --detach --build` or `docker compose --file compose-multifeed.yaml up --detach --build`
- `docker compose up --detach --build --force-recreate` or `docker compose --file compose-multifeed.yaml up --detach --build --force-recreate`

### monitor all ADSB and OGN traffic consolidated in a single tar1090 instance
- `http://yourReceiverIP.local/tar1090`

### enable DE and AT traffic patterns
- quick hack for now: enable "UK Radar Corridors":
<img width="510" height="346" alt="DE AT Traffic Patterns" src="https://github.com/user-attachments/assets/a9db25d0-0659-48ce-99eb-3277e88ea54e" />

### monitor OGN details
- `http://yourReceiverIP:8080`
- `http://yourReceiverIP:8081`

### monitor docker containers
- `docker logs -f rtlsdr-ogn`
- `docker logs -f mlat-client-adsbx`
- `docker logs -f readsb`
- `docker logs -f ogn2dump1090`
- `docker logs -f tar1090`

### useful docker commands
- `docker ps -a` list all docker containers, including stopped ones
- stop and deactivate containers
  - `docker stop <container_name_or_id>` stop a running container
  - `docker rm <container_name_or_id>` deactivate a stopped container
  - `docker container prune` remove all stopped containers
  - `docker compose down` stop and remove containers, networks
  - `docker compose up --detach` create and start containers
  - `docker compose up --detach --build` build, create and start containers
- list and delete docker images
  - `docker image ls` list docker images
  - `docker rmi <image_id_or_name>` delete docker image
  - `docker image prune` delete all docker images
- clean your entire docker environment e.g. for a fresh `docker compose`
  - `docker rm -f $(docker ps -aq)` force remove ALL containers
  - `docker system prune -af --volumes` clean your docker environment
- open a shell inside your container
  - `docker exec -it <yourDockerContainer> bash`
