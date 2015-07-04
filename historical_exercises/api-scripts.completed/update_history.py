#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.histories.HistoriesController.update
# lib/galaxy/webapps/galaxy/api/histories.py, def update
def update_history( id, update_json ):
    # we need to specify which history to change/edit/update - so again we add the id
    full_url = BASE_URL + '/api/histories/' + id

    # in the case of put we'll send both params and data
    params = {
        'key' : open( '.api-key' ).readline().strip(),
    }
    # PUT + RESOURCE + ID == update
    return requests.put( full_url, params=params, data=update_json )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = update_history( sys.argv[1], sys.argv[2] )
    output.output_response( response )
