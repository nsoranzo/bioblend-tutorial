#!/usr/bin/env python

import sys
import os
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def upload_file_as_another_user( user_id, history_id, filepath, **kwargs ):
    full_url = BASE_URL + '/api/tools'

    inputs = {
        'files_0|type'  : 'upload_dataset',
        'ajax_upload'   : u'true',
        'files_0|NAME'  : os.path.basename( filepath ),
        'dbkey'         : '?',
        'file_type'     : 'auto',
    }
    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        'tool_id'       : 'upload1',
        'history_id'    : history_id,
        'inputs'        : json.dumps( inputs ),
        
        # by sending the additional param 'run_as', (and if we have api_allow_run_as set to our email),
        #   we can tell Galaxy to upload a file as another user
        'run_as'        : user_id
    }

    response = None
    with open( filepath, 'rb' ) as file_to_upload:
        files = { 'files_0|file_data' : file_to_upload }
        response = requests.post( full_url, data=data, files=files )
    return response


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    run_as_email, history_id, filepath = sys.argv[1:4]
    response = upload_file( user_id, history_id, filepath )
    output.output_response( response )
