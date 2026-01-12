FROM debian:trixie-slim
WORKDIR /app

RUN apt-get update && apt-get install --yes \
    chrony telnet libpng16-16 wget gettext-base librtlsdr-dev librtlsdr0 rtl-sdr socat moreutils procserv

RUN bash -c 'if [[ "$(arch)" == *x86* ]]; then \
        wget "http://download.glidernet.org/x64/rtlsdr-ogn-bin-x64-latest.tgz"; \
    else \
        wget "https://github.com/VirusPilot/ogn-pi34/raw/master/rtlsdr-ogn-bin-arm64-0.3.3_Trixie.tgz"; \
    fi'

RUN tar xzf rtlsdr-ogn-*.tgz && \
    rm rtlsdr-ogn-*.tgz

COPY ogn-template.conf /app/

COPY startup.sh /app/

RUN \
    cd rtlsdr-ogn && \
    wget http://download.glidernet.org/common/WW15MGH.DAC  && \
    cp -v rtlsdr-ogn /etc/init.d/rtlsdr-ogn && \
    cp -v rtlsdr-ogn.conf /etc/rtlsdr-ogn.conf && \
    sed -i "s|/home/pi/rtlsdr-ogn|/app/rtlsdr-ogn|g" /etc/rtlsdr-ogn.conf && \
    sed -i "s| pi | root |g" /etc/rtlsdr-ogn.conf

CMD ["/app/startup.sh"]
