### NOTE: upgrading from an earlier version
if you are upgrading from an earlier version, particularly in case the `config.vars` template has changed, you need to perform the following steps:
- note down your existing `config.vars` variable entries
- `git checkout config.vars`
- `git pull`
- re-enter your prior variable entries in  the new and empty `config.vars` and fill out the new (optional) config variables
- `docker compose --detach --build` (without optional feeds) or
- `docker compose --file compose-multifeed.yaml up --detach --build` (with optional feeds)

### docker version of [ogn2readsb](https://github.com/b3nn0/ogn2dump1090)
consisting of the following components:
- [ogn2dump1090](https://github.com/b3nn0/ogn2dump1090)
  - simple Python tool to inject Open Glider Network Traffic (from an existing local OGN decoder instance) into an existing readsb ADS-B decoder instance for display on a unified tar1090 map
  - furthermore online aggregated traffic from `aprs.glidernet.org` can optionally be injected for a reasonably selected radius around a given location
  - OGN traffic will be displayed as other traffic alongside with ADS-B traffic, using the readsb tar1090 webinterface (e.g. http://yourRaspberryPi.local/tar1090/)
- [rtlsdr-ogn](https://github.com/VirusPilot/ogn-pi34) (feeding glidernet.org with OGN traffic)
- [readsb](https://github.com/wiedehopf/readsb) (feeding glidernet.org with ADS-B traffic and decoding/forwarding traffic to the tar1090 map)
- [mlat-client-adsbx](https://github.com/wiedehopf/mlat-client) (display MLAT traffic from adsbexchange.com)
- [tar1090](https://github.com/wiedehopf/tar1090) (traffic map)
- optional feeds:
  - adsbexchange.com
  - airplanes.live
  - adsb.lol
  - adsb.fi
  - planefinder.net
  - flightradar24.com
  - airnavradar.com
  - flightaware.com
  - opensky-network.org

![ogn2readsb](https://github.com/user-attachments/assets/0e3c71e2-113a-4b45-88c6-007bedd7a064)
### supported operating systems
Debian or Debian-based Linux Operating Systems (64bit Debian 13 Trixie or newer):
- Debian
- Ubuntu
- DietPi
- RaspiOS

### supported hardware architectures
- arm64 (64-bit ARM CPUs with hardware floating point processor)
- x64 (64-bit AMD/Intel CPUs)
- SDRs: native support of RTL-SDR Blog v4 SDR since Debian 13 Trixie

### prepare system and docker
- `sudo apt update && sudo apt install --yes git wget`
- `bash <(wget -q -O - https://raw.githubusercontent.com/VirusPilot/docker-install/main/docker-install.sh)`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

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
| STATION_COMMENT_ANTENNA | VINNANT CC868/8-PEL | optional information about your station antenna | 
| STATION_COMMENT_FILTER |  | optional information about your station filter | 
| STATION_COMMENT_AMPLIFIER | Uputronics HAB-FPA868 | optional information about your station amplifier | 
| STATION_COMMENT_DONGLE | rtl-sdr v3 silver | optional information about your station dongle| 
| STATION_COMMENT_CLUB |  | optional name of your Flight Club | 
| STATION_COMMENT_EMAIL |  | optional station email contact| 
| STATION_COMMENT_WEBSITE |  | optional station website | 
| STATION_COMMENT_NOTE |  | optional notes about your station | 
| FREQ_PLAN | 1 | 1=EU/Africa (default), 2=USA/Canada, 3=South America/Australia, 4=New Zealand, 5=Israel, 6=EU/Africa 433MHz |
| GSM_CENTER_FREQ | 935.8 | default = 0, change only if you know your closest GSM900 station frequency [MHz] |
| ADSB_MAX_ALT_FT | 18000 | ADSB max OGN feed altitude [ft] |
| METAR_SOURCE_ICAO | EDDF | 4 letter ICAO code of a nearby airport with [METAR](https://aviationweather.gov) service |
| APRS_SUBSCRIBE_FILTER | r/50.0/10.0/100 | circle in [km] around a defined postion (example: LAT 50.0, LON 10.0, CIRCLE 100 km) for which you want to receive traffic from the OGN APRS servers |
| SDR_868_SERIAL | 868 | enter your OGN SDR serial |
| SDR_868_PPM | 0 | change only if you know your SDR's ppm |
| SDR_868_BIAS_T_ENABLE | 0 | set to 1 to enable Bias Tee on your SDR, e.g. to power a LNA |
| SDR_1090_SERIAL | 1090 | enter your ADSB SDR serial |
| SDR_1090_PPM | 0 | change only if you know your SDR's ppm |
| SDR_1090_BIAS_T_ENABLE | 0 | set to 1 to enable Bias Tee on your SDR, e.g. to power a LNA |

### option to merge inconsistent address type transmissions
- `cd ./docker-ogn2readsb`
- `nano tar1090/Dockerfile`
-  add ` && echo 'MergeNonIcao = true;' >> config.js` after `echo 'jaeroLabel = "OGN";' >> config.js`

### build (only feeding glidernet)
- `cd ./docker-ogn2readsb`
- `docker compose up --detach --build`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

### ADVANCED build (with addidtional feeders)
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
- standard build
  - `docker compose up --detach --build` or
  - `docker compose --file compose-multifeed.yaml up --detach --build`
- build with `--force-recreate`
  - `docker compose up --detach --build --force-recreate` or
  - `docker compose --file compose-multifeed.yaml up --detach --build --force-recreate`
- if you are building an update over an ssh shell that may lose its connection, please consider using `nohup <your command> &`

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
- list and delete unused docker images
  - `docker image ls` list docker images
  - `docker rmi <image_id_or_name>` delete unused docker image
  - `docker image prune` delete all unused docker images
- remove unused data e.g. to save space
  - `docker system prune`
- clean your entire docker environment e.g. for a fresh `docker compose`
  - `docker rm -f $(docker ps -aq)` force remove ALL containers
  - `docker system prune -af --volumes` clean your docker environment
- open a shell inside your container
  - `docker exec -it <yourDockerContainer> bash`
