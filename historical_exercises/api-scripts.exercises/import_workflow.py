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

    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        #EXERCISE: send workflow json as text value
        'workflow'       : #...
    }
    #EXERCISE: return ...


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = import_workflow( sys.argv[1] )
    output.output_response( response )
