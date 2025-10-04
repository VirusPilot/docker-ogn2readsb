FROM debian:trixie
WORKDIR /app

RUN apt update && \
    apt install --yes git python3-venv python3-setuptools python3-pip python3-dev build-essential moreutils

RUN pip install --break-system-packages pyasyncore

ADD https://api.github.com/repos/wiedehopf/mlat-client/git/refs/heads/master version.txt

RUN git clone https://github.com/wiedehopf/mlat-client && \
    cd mlat-client && \
    python3 setup.py build && \
    python3 setup.py install && \
    cd .. && \
    rm -r mlat-client

CMD ["bash", "-c", "mlat-client --lat ${STATION_LAT} --lon ${STATION_LON} --alt ${STATION_ALT_MSL_M} --user ${STATION_NAME} --server ${MLATSERVER} \
 --input-type auto --no-udp --input-connect ${BEAST_OUT_HOST} --results beast,connect,${BEAST_IN_HOST} 2>&1 | ts"]
