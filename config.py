# from flask import Flask, jsonify, request
import os
import logging


NEW_RELIC_LICENSE_KEY:str|None = None
SHELLY_PLUG_IP:str|None = None
SHELLY_PLUG_INTERVAL:int = -1



def init():
    global NEW_RELIC_LICENSE_KEY
    global SHELLY_PLUG_IP
    global SHELLY_PLUG_INTERVAL

    init_logger()
    logger = logging.getLogger(__name__)

    NEW_RELIC_LICENSE_KEY=os.environ.get("NEW_RELIC_LICENSE_KEY")
    if (NEW_RELIC_LICENSE_KEY == None):
        logger.fatal('FATAL - env NEW_RELIC_LICENSE_KEY not defined - Exit service')
        quit()
        
    SHELLY_PLUG_IP = os.environ.get("SHELLY_PLUG_IP")
    if (SHELLY_PLUG_IP == None):
        logger.fatal('FATAL - env SHELLY_PLUG_IP not defined - Exit service')
        quit()

    env_value = os.environ.get("SHELLY_PLUG_INTERVAL")
    if (env_value == None):
        logger.fatal('FATAL - env SHELLY_PLUG_INTERVAL not defined - Exit service')
        quit()
    else:
        try:
            SHELLY_PLUG_INTERVAL = int(env_value)
        except ValueError:
            logger.fatal(f'FATAL - env SHELLY_PLUG_INTERVAL value "{env_value}" is not an integer - Exit service')
            quit()


def init_logger():

    # Configure logging for __main__ logger
    logging.basicConfig(
        level=logging.INFO,  # Show INFO and above
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
