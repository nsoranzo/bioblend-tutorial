#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.histories.HistoriesController.show
# lib/galaxy/webapps/galaxy/api/histories.py, def show
def show_history( id ):
    # specify which history by adding the id to the resource URL
    full_url = BASE_URL + '/api/histories/' + id

    params = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    # GET + RESOURCE + ID == show
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = show_history( sys.argv[1] )
    output.output_response( response )
