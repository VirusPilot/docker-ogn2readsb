### initial commit
### steps
- `sudo apt update && sudo apt install git`
- `git clone https://github.com/VirusPilot/docker-ogn2readsb`
- `cd docker-ogn2readsb`
- `sudo usermod -aG docker $USER`
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)`
- `nano compose.yml` (modify accordingly, e.g. SDR_868_SERIAL, METAR_SOURCE_ICAO, APRS_SUBSCRIBE_FILTER)
- `nano config.vars` (modify accordingly,e.g. STATION_NAME)
- `docker compose up -d`
- `sudo reboot`
- `https://yourRaspberryPi.local/tar1090`
