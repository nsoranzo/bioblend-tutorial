#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.histories.HistoriesController.create
# lib/galaxy/webapps/galaxy/api/histories.py, def create
def create_history( *args ):
    # we're making a new history - so we have no id to pass
    full_url = BASE_URL + '/api/histories'

    #params = {
    #    'key'           : open( '.api-key' ).readline().strip(),
    #}
    data = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    # POST + RESOURCE == create
    #return requests.post( full_url, params=params, data=data )
    return requests.post( full_url, data=data )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = create_history( *sys.argv[1:] )
    output.output_response( response )
