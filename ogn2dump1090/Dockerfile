FROM debian:trixie-slim
WORKDIR /app

RUN apt update && apt install --yes \
    git python3-pip wget gettext-base  python3-aiohttp

RUN pip install --break-system-packages ogn-client

ADD https://api.github.com/repos/b3nn0/ogn2dump1090/git/refs/heads/master version.txt

RUN git clone https://github.com/b3nn0/ogn2dump1090
COPY ogn2dump1090_config.py /app/

ADD http://ddb.glidernet.org/download/?j=1 ogn2dump1090/ddb.json

CMD ["bash", "-c", "envsubst < ogn2dump1090_config.py > ogn2dump1090/config.py && cd ogn2dump1090 && ./ogn2dump1090.py"]
