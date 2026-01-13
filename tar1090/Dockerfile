FROM debian:trixie-slim
WORKDIR /app

RUN apt-get update && apt-get install --yes \
    nginx curl

ADD https://api.github.com/repos/wiedehopf/tar1090/git/refs/heads/master version.txt

ADD https://github.com/wiedehopf/tar1090/raw/master/install.sh install.sh

RUN chmod +x install.sh && ./install.sh /tmp/readsb

COPY Platzrunden+Segler_N_5.25.5.geojson /app/
RUN cp -f Platzrunden+Segler_N_5.25.5.geojson /usr/local/share/tar1090/html/geojson/UK_Mil_RC.geojson

COPY etc_nginx_sites-enabled_default /app/
RUN cp -f etc_nginx_sites-enabled_default /etc/nginx/sites-enabled/default

RUN cd /usr/local/share/tar1090/html && \
    echo 'jaeroTimeout = 60;' >> config.js && \
    echo 'jaeroLabel = "OGN";' >> config.js

ADD startup.sh startup.sh

CMD ["/bin/bash", "/app/startup.sh"]
