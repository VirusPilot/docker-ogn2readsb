FROM debian:bookworm
WORKDIR /app

RUN \
    apt update && \
    apt install --no-install-recommends --no-install-suggests --yes \
        git librtlsdr-dev librtlsdr0 build-essential libusb-1.0-0-dev pkg-config libncurses-dev zlib1g-dev zlib1g libzstd-dev libzstd1 ca-certificates

ADD https://api.github.com/repos/wiedehopf/readsb/git/refs/heads/dev version.txt

RUN \
    git clone https://github.com/wiedehopf/readsb.git && \
    cd readsb && \
    make -j8 RTLSDR=yes && \
    cp readsb /usr/local/bin && \
    rm -r /app/readsb

CMD ["bash", "-c", "readsb --lat ${STATION_LAT} --lon ${STATION_LON} ${RECEIVER_OPTIONS} --device ${SDR_1090_SERIAL} --ppm ${SDR_1090_PPM} ${DECODER_OPTIONS} ${NET_OPTIONS} ${JSON_OPTIONS} ${FEEDER_1} ${FEEDER_2} ${FEEDER_3} ${FEEDER_4}"]
