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
    #EXERCISE: we need to specify which history to change/edit/update - so again we add the id
    full_url = #...

    params = {
        'key' : open( '.api-key' ).readline().strip(),
    }
    # in the case of put we'll send both params and data
    # PUT + RESOURCE + ID == update
    #EXERCISE: ... params=params, data=update_json )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = update_history( sys.argv[1], sys.argv[2] )
    output.output_response( response )
