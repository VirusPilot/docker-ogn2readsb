FROM debian:bookworm
WORKDIR /app

RUN apt update && \
    apt -y install ntp ntpdate telnet libpng16-16 wget gettext-base librtlsdr0 socat moreutils procserv

RUN \
    wget "http://download.glidernet.org/arm64/rtlsdr-ogn-bin-arm64-latest.tgz"; \
    tar xzf rtlsdr-ogn-*.tgz && \
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