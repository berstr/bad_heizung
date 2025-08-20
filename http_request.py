import logging
import requests
import json
from typing import  Dict

logger = logging.getLogger() 


def http_request(url:str, params:Dict, headers:Dict, timeout:int) -> Dict:
     
    """ makes a HTTP Get request

        Raises:
            ConnectionError , Timeout, NonJSONResponseError
    """

    '''
    resultx:HttpResponseT = {
        "status" : RequestStatusT.SUCCESS,
        "result": None,
        "error": None
    }
'''
    
    result : Dict

    try:

        #req = requests.Request("GET", url, params=params).prepare()
        
        # Send the GET request
        response = requests.get(url, params=params, headers=headers, timeout=(5,timeout)) #  5 seconds to connect, X seconds to wait for a response

        result = response.json()
        logger.debug("requests.get() - json response: %s",json.dumps(result))

 
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx), include response object in exception
    
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.Timeout(f"cannot connect to url: {url}")

    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout(f"timeout after {timeout} second - url: {url}")


    return result




