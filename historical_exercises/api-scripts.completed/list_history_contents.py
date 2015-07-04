#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.history_contents.HistoryContentsController.index
# lib/galaxy/webapps/galaxy/api/history_contents.py, def index
def list_history_contents( history_id ):
    # here we take the normal resource + id (of history show) and further specify
    #   by adding '/contents'. This tells the API we're interested in the contents
    #   of that history (HistoryDatasetAssociations, etc.)
    full_url = BASE_URL + '/api/histories/' + history_id + '/contents'

    params = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    # GET + RESOURCE + ID == show
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = list_history_contents( sys.argv[1] )
    output.output_response( response )
