### initial commit, not working for now !!!
### steps
- `sudo apt update`
- `sudo usermod -aG docker $USER`
- `bash <(wget -q -O - https://raw.githubusercontent.com/sdr-enthusiasts/docker-install/main/docker-install.sh)` without SDR driver setup
- `nano compose.yml`
- `nano config.vars`
- `docker compose up -d`
