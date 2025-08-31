### docker version of https://github.com/b3nn0/ogn2dump1090

### supported platforms
- arm64 (64-bit ARM CPUs with hardware floating point processor)
- amd64 (64-bit Intel CPUs)

### prepare
- `sudo apt update && sudo apt install git`
- `git clone https://github.com/VirusPilot/docker-ogn2readsb`
- `cd docker-ogn2readsb`
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)`
- `sudo usermod -aG docker $USER && newgrp docker`

### configuration
- `nano config.vars`
  - STATION_LAT=**50.0** <--- enter your station latitude
  - STATION_LON=**10.0** <--- enter your station longitude
  - STATION_ALT_MSL_M=**300** <--- enter your sattion altitude [m] AMSL
  - STATION_NAME=**OGNTEST** <--- enter your station name, please refer to http://wiki.glidernet.org/receiver-naming-convention
  - METAR_SOURCE_ICAO=**ETHN** <--- enter the closest airport with METAR
  - APRS_SUBSCRIBE_FILTER=**r/50.0/10.0/100** <--- circle in [km] for which you want to receive traffic from the OGN APSR servers
  - SDR_868_SERIAL=**868** <--- enter your OGN SDR serial
  - SDR_868_PPM=**0** <--- change only if you know your SDR's ppm
  - SDR_1090_SERIAL=**1090** <--- enter your ADSB SDR serial
  - SDR_1090_PPM=**0** <--- change only if you know your SDR's ppm

### build
- `docker compose up --detach --build`
- `sudo reboot`

### monitor all ADSB and OGN traffic consolidated in a single tar1090 instance
- `http://yourRaspberryPi.local/tar1090`
