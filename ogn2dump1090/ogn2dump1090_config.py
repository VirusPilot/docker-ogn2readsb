# Host/Port where readsb is running with something like --net-sbs-in-port=30008
sbs_destination_host = "${SBS_DESTINATION_HOST}"
sbs_destination_port = ${SBS_DESTINATION_PORT}

# Host/Port where ogn-decode telnet listens. Leave empty or set to None if you only want APRS functionality
TELNET_SERVER_HOST = "${OGN_DECODE_TELNET_HOST}"
TELNET_SERVER_PORT = ${OGN_DECODE_TELNET_PORT}

# Use generic APRS Server address instead of the list above
aprs_servers = ['aprs.glidernet.org']

# Subscribe to positions with a 20km radius around the given location. None if you don't want to subscribe to anything
aprs_subscribe_filter = "${APRS_SUBSCRIBE_FILTER}"

# Optional:
# ADS-B Data is usually based on pressure altitude, but OGN is based on GPS altitude.
# ogn2dump1090 can convert it for you, by fetching METARS from a nearby airport via https://aviationweather.gov/data/api/
# Must be the 4 letter ICAO code of a nearby airport, e.g. "EDNY". Test the request via https://aviationweather.gov/api/data/metar?ids=EDNY
metar_source = "${METAR_SOURCE_ICAO}"
