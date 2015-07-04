#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def list_workflows():
    # http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.workflows.WorkflowsAPIController.index
    # lib/galaxy/webapps/galaxy/api/workflows.py, def index
    full_url = BASE_URL + '/api/workflows'

    params = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = list_workflows()
    output.output_response( response )
