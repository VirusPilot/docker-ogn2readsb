#!/bin/bash

envsubst < /app/ogn-template.conf > /app/rtlsdr-ogn/Template.conf

/etc/init.d/rtlsdr-ogn start

cd /app/rtlsdr-ogn

# debians procServ can't listen publically.. proxy it
socat TCP-LISTEN:50001,fork,bind=$(hostname -i) TCP4:localhost:50001
