#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def import_workflow( filepath ):
    # http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.workflows.WorkflowsAPIController.import_new_workflow
    # lib/galaxy/webapps/galaxy/api/workflows.py, def import_new_workflow
    full_url = BASE_URL + '/api/workflows/upload'

    workflow_json = open( filepath ).read()
    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        'workflow'       : workflow_json
    }
    return requests.post( full_url, data=data )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = import_workflow( sys.argv[1] )
    output.output_response( response )
