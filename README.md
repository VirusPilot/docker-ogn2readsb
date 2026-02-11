### NOTE: major changes as of 11 Feb, 2026
the following upgrade steps are required:
- `cd ./docker-ogn2readsb`
- `git pull`
- `docker rm -f $(docker ps -aq)`
- `docker system prune -af --volumes`
- `docker compose --parallel 1 build` (or `docker compose --file compose-multifeed.yaml --parallel 1 build`)
- `docker compose --parallel 1 up --detach --force-recreate` (or `docker compose --file compose-multifeed.yaml --parallel 1 up --detach --force-recreate`)
### NOTE: upgrading from an earlier `config.vars` version
if you are upgrading from an earlier `config.vars` version, particularly in case the `config.vars` template has changed, you need to perform the following steps:
- note down your existing `config.vars` variable entries
- `cd ./docker-ogn2readsb`
- `git checkout config.vars`
- `git pull`
- `nano config.vars`
- re-enter your prior variable entries in  the new and empty `config.vars` and fill out the new (optional) config variables
- `docker compose --parallel 1 up --detach --force-recreate` (or `docker compose --file compose-multifeed.yaml --parallel 1 up --detach`)
---
### docker version of [ogn2readsb](https://github.com/b3nn0/ogn2dump1090)
consisting of the following components:
- [ogn2dump1090](https://github.com/b3nn0/ogn2dump1090)
  - simple Python tool to inject Open Glider Network Traffic (from an existing local OGN decoder instance) into an existing readsb ADS-B decoder instance for display on a unified tar1090 map
  - furthermore online aggregated traffic from `aprs.glidernet.org` can optionally be injected for a reasonably selected radius around a given location
  - OGN traffic will be displayed as other traffic alongside with ADS-B traffic, using the readsb tar1090 webinterface (e.g. http://yourRaspberryPi.local/tar1090/)
- [rtlsdr-ogn](https://github.com/VirusPilot/ogn-pi34) (feeding glidernet.org with OGN traffic)
- [readsb](https://github.com/wiedehopf/readsb) (feeding glidernet.org with ADS-B traffic and decoding/forwarding traffic to the tar1090 map)
- [mlat-client-adsblol](https://github.com/wiedehopf/mlat-client) (display MLAT traffic from adsb.lol)
- [tar1090](https://github.com/wiedehopf/tar1090) (traffic map)
- optional feeds (advanced docker build):
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
---
### supported hardware architectures
- arm64 (64-bit ARM CPUs with hardware floating point processor)
- x64 (64-bit AMD/Intel CPUs)
- SDRs: native support of RTL-SDR Blog v4 SDR since Debian 13 Trixie

### prepare system and docker
- `sudo apt update && sudo apt install --yes git wget`
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)`
- you may be asked `Y/n` a couple of times, it is safe to answer all of them with `Y`
- `sudo reboot`

### prepare SDR_868_SERIAL and SDR_1090_SERIAL
- identify or set both SDR serials (e.g. 868 and 1090), they are required for the `config.vars` below
- unplug all SDRs, leaving only the SDR to be used for 868 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_eeprom ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -s 868` 
- unplug all SDRs, leaving only the SDR to be used for 1090 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_eeprom ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -s 1090`

### prepare SDR_868_PPM and SDR_1090_PPM
- unplug all SDRs, leaving only the SDR to be used for 868 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_test ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -p`
  - let it run for 10-15 min (important so that the SDR warms up)
  - note the ppm listed in the related output, e.g. `... cumulative PPM: -1` and use that for SDR_868_PPM
  - modern SDRs have a TCXO, therefore SDR_868_PPM = 0 is the default
- unplug all SDRs, leaving only the SDR to be used for 1090 MHz reception plugged in, then issue the following command:
  - `docker run --rm -it --device /dev/bus/usb --entrypoint rtl_test ghcr.io/sdr-enthusiasts/docker-adsb-ultrafeeder -p`
  - let it run for 10-15 min (important so that the SDR warms up)
  - note the ppm listed in the related output, e.g. `... cumulative PPM: -1` and use that for SDR_1090_PPM
  - modern SDRs have a TCXO, therefore SDR_1090_PPM = 0 is the default

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

### standard build (only feeding glidernet and adsb.lol)
- `cd ./docker-ogn2readsb`
- `docker compose --parallel 1 build`
- `docker compose --parallel 1 up --detach --force-recreate`

### advanced build (with addidtional feeders)
- quite some manual editing is required, please use it only if you know what you are doing
- `cd ./docker-ogn2readsb`
- `nano compose-multifeed.yaml`
  - add your feeder credentials (e.g. SHARING KEY, USERNAME, LAT, LON, ALT)
  - delete (or comment out) unused/unwanted feeder entries
- `docker compose --file compose-multifeed.yaml --parallel 1 build`
- `docker compose --file compose-multifeed.yaml --parallel 1 up --detach --force-recreate`
---
### apply configuration changes
- `cd ./docker-ogn2readsb`
- `nano config.vars`
- `docker compose --parallel 1 up --detach --force-recreate` (or `docker compose --file compose-multifeed.yaml --parallel 1 up --detach --force-recreate`)

### monitor all ADSB and OGN traffic consolidated in a single tar1090 instance
- `http://yourReceiverIP.local/tar1090`

### enable DE and AT traffic patterns
- quick hack for now: enable "UK Radar Corridors":
<img width="510" height="346" alt="DE AT Traffic Patterns" src="https://github.com/user-attachments/assets/a9db25d0-0659-48ce-99eb-3277e88ea54e" />

### disable local APRS Proxy Server
- `nano compose.yaml` or `nano compose-multifeed.yaml`
- in section `rtlsdr-ogn:environment:` replace `APRS_SERVER=ogn2dump1090:14580` with `APRS_SERVER=aprs.glidernet.org:14580`
- `docker compose --parallel 1 up --detach --force-recreate` or `docker compose --file compose-multifeed.yaml --parallel 1 up --detach --force-recreate`

### monitor OGN details
- `http://yourReceiverIP:8080`
- `http://yourReceiverIP:8081`

### monitor docker containers
- `docker compose logs -f` or `docker compose --file compose-multifeed.yaml logs -f` (monitor all containers)
- `docker logs -f rtlsdr-ogn`
- `docker logs -f mlat-client-adsblol`
- `docker logs -f readsb`
- `docker logs -f ogn2dump1090`
- `docker logs -f tar1090`

### monitor docker statistics
- `docker stats` (`CTRL C` to exit)

### open a shell inside your container
- `docker exec -it <yourDockerContainer> bash`

### useful docker commands (examples for standard build)
- `docker ps -a` list all docker containers, including stopped ones
- docker **container** related commands
  - `docker stop <container_name_or_id>` stop a running container
  - `docker rm <container_name_or_id>` deactivate a stopped container
  - `docker container prune` remove all stopped containers
  - `docker compose down` stop and remove all containers and networks
  - `docker compose build --no-cache` only build images
  - `docker compose up --detach --build --force-recreate` create images and start containers
  - `docker compose up --detach --force-recreate` recreate and start containers
- docker **image** related commands
  - `docker image ls` list docker images
  - `docker rmi <image_id_or_name>` delete docker image
  - `docker image prune` delete all unused docker images
- docker **system** related commands
  - `docker system prune` clean your docker environment
- clean your entire docker environment e.g. for a fresh setup
  - `docker rm -f $(docker ps -aq)` force remove ALL containers
  - `docker system prune -af --volumes` clean your entire docker environment

 ### docker terms and related meaning
| Term       | Meaning                                              |
| ---------- | ---------------------------------------------------- |
| Dockerfile | Build instructions                                   |
| Image      | Built / immutable system image                       |
| Container  | Running instance of an image                         |
| Compose    | Orchestration / startup plan for multiple containers |
