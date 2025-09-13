FROM debian:bookworm
WORKDIR /app

RUN \
    apt update && \
    apt install --yes \
        nginx curl

ADD https://api.github.com/repos/wiedehopf/tar1090/git/refs/heads/master version.txt

ADD https://github.com/wiedehopf/tar1090/raw/master/install.sh install.sh

RUN chmod +x install.sh && ./install.sh /tmp/readsb

RUN sed -i 's|root /var|include /usr/local/share/tar1090/nginx-tar1090.conf;\nroot /var|g' /etc/nginx/sites-enabled/default

RUN cd /usr/local/share/tar1090/html && \
    echo 'jaeroTimeout = 60;' >> config.js && \
    echo 'jaeroLabel = "OGN";' >> config.js

ADD startup.sh startup.sh

CMD ["/bin/bash", "/app/startup.sh"]
