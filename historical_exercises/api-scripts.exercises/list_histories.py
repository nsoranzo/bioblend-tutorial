#!/usr/bin/env python

import sys
import json
import requests
import output

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.histories.HistoriesController.index
# lib/galaxy/webapps/galaxy/api/histories.py, def index
def list_histories():
    # listing/index of all histories
    full_url = BASE_URL + '/api/histories'

    params = {
        # read the key from the .api-key file
        'key'           : open( '.api-key' ).readline().strip(),
    }
    # GET plus resource == index/list of all resources of that kind
    return requests.get( full_url, params=params )
    # --> HTTP GET 'http://localhost:8080/api/histories?key=<your api key>'


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = list_histories()
    output.output_response( response )
