import logging
import requests
import time

from http_request import http_request
import config


config.init()

logger = logging.getLogger(__name__)

logger.info("STARTUP - Bad Heizung Monitor")


def turn_off():
    url = f'http://192.168.178.203/relay/0\?turn=off'
    resp = http_request(url, {}, {}, 5 )


timer = 0

while True:
    print("Running task at", time.strftime("%Y-%m-%d %H:%M:%S"))
    
    url = f'http://{config.SHELLY_PLUG_IP}/status'

    try:
        resp = http_request(url, {}, {}, 5 )

    except requests.exceptions.Timeout as e:   
        logger.error(f"Request timed out: {e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error: {e}")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    else: 
        power = resp['meters'][0]['power']
        ison = resp['relays'][0]['ison']

        logger.info(f"shelly plug- ison: {ison} - power: {power}")

        if ison == True:
            timer += 1

            if timer >= 3:
                turn_off()
                timer = 0
        else:
            timer = 0


    time.sleep(config.SHELLY_PLUG_INTERVAL)
