# Host/Port where readsb is running with something like --net-sbs-in-port=30008
sbs_destination_host = "${SBS_DESTINATION_HOST}"
sbs_destination_port = ${SBS_DESTINATION_PORT}

# Host/Port where ogn-decode telnet listens. Leave empty or set to None if you only want APRS functionality
TELNET_SERVER_HOST = "${OGN_DECODE_TELNET_HOST}"
TELNET_SERVER_PORT = ${OGN_DECODE_TELNET_PORT}

# Use generic APRS Server address instead of the list above
aprs_servers = ['aprs.glidernet.org']

# DroneAware UDP port. Supports forwarding DroneAware data to readsb, too.
# Disabled by default. Set to 9999 to enable (listens for UDP broadcasts of DroneAware)
DRONEAWARE_UDP_PORT = ${DRONEAWARE_UDP_PORT}

# Subscribe to positions with a 20km radius around the given location. None if you don't want to subscribe to anything
aprs_subscribe_filter = "${APRS_SUBSCRIBE_FILTER}"

# Optional:
# ADS-B Data is usually based on pressure altitude, but OGN is based on GPS altitude.
# ogn2dump1090 can convert it for you, by fetching METARS from a nearby airport via https://aviationweather.gov/data/api/
# Must be the 4 letter ICAO code of a nearby airport, e.g. "EDNY". Test the request via https://aviationweather.gov/api/data/metar?ids=EDNY
metar_source = "${METAR_SOURCE_ICAO}"

# If set to True, aircraft addresses indicated as non-icao will receive a "~" prefix for readsb to not merge them with
# a potential ICAO address aircraft.
# If set to false, all OGN addresses are passed as if they were ICAO adresses.
# This mainly helps with SafeSky targets when an aprs_subscribe_filter is set. These
# ALWAYS report as OGN adresses, despite actually being valid ICAO adresses.
respect_ogn_address_type = ${RESPECT_OGN_ADDRESS_TYPE}
