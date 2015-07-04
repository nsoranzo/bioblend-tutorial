#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def show_workflow( workflow_id ):
    # http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.workflows.WorkflowsAPIController.show
    # lib/galaxy/webapps/galaxy/api/workflows.py, def import
    full_url = BASE_URL + '/api/workflows/' + workflow_id

    params = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = show_workflow( sys.argv[1] )
    output.output_response( response )
