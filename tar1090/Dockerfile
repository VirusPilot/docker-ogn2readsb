FROM debian:bookworm
WORKDIR /app

RUN \
    apt update && \
    apt install --yes \
        nginx curl gdal-bin wget

ADD https://api.github.com/repos/wiedehopf/tar1090/git/refs/heads/master version.txt

ADD https://github.com/wiedehopf/tar1090/raw/master/install.sh install.sh

RUN chmod +x install.sh && ./install.sh /tmp/readsb

RUN wget -O Platzrunden_5.25.1.kml "https://www.dropbox.com/scl/fo/4t4x4y4ip8pujkpcea89t/ACKrMvNdW6InwtuL9dJLDh0/Platzrunden%2BSegler_5.25.1.kml?rlkey=h47rcbgi0qfuojjtgdhnfq21g&dl=1"

RUN ogr2ogr -f "GeoJSON" UK_Mil_RC.geojson Platzrunden_5.25.1.kml

RUN cp -f UK_Mil_RC.geojson /usr/local/share/tar1090/html/geojson/

RUN sed -i 's|root /var|include /usr/local/share/tar1090/nginx-tar1090.conf;\nroot /var|g' /etc/nginx/sites-enabled/default

RUN cd /usr/local/share/tar1090/html && \
    echo 'jaeroTimeout = 60;' >> config.js && \
    echo 'jaeroLabel = "OGN";' >> config.js

ADD startup.sh startup.sh

CMD ["/bin/bash", "/app/startup.sh"]
