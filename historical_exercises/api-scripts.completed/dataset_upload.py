#!/usr/bin/env python

import sys
import os
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def upload_file( history_id, filepath, **kwargs ):
    # the upload tool is essentially the same as any other tool:
    #   it accepts parameters and starts a job using the desired tool (in this case, upload1)
    #   in galaxy's job handling system
    # the main difference being we send our file (as data) as another parameter using HTTP
    full_url = BASE_URL + '/api/tools'

    # these are the tool parameters - in the case of upload, some must be set as
    #   below; others are changable
    inputs = {
        # these are not changable
        'files_0|type'  : 'upload_dataset',
        'ajax_upload'   : u'true',
        # name - changable
        'files_0|NAME'  : os.path.basename( filepath ),
        # db to assign - changable
        'dbkey'         : '?',
        # datatype to assign - changable
        'file_type'     : 'auto',
    }
    data = {
        # like any post, the api key can go directly into the data
        'key'           : open( '.api-key' ).readline().strip(),
        # the id of the upload tool - tool ids are more human readable but don't
        #   always correspond to the name in the tool panel; use api/tools to get more info
        'tool_id'       : 'upload1',
        # to which history are we uploading?
        'history_id'    : history_id,
        # for many tools the inputs need to be sent as a json encoded string
        'inputs'        : json.dumps( inputs )
    }

    # for upload, we're using a special post parameter named 'files' which allows
    #   us to attach the file data to the request
    # requests makes this much easier than urllib or other libraries
    response = None
    with open( filepath, 'rb' ) as file_to_upload:
        files = { 'files_0|file_data' : file_to_upload }
        response = requests.post( full_url, data=data, files=files )
    return response


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    history_id, filepath = sys.argv[1:3]
    response = upload_file( history_id, filepath )
    output.output_response( response )
