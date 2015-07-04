#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def list_tools():
    full_url = BASE_URL + '/api/tools/'

    params = {
        'key' : open( '.api-key' ).readline().strip(),
        'in_panel' : False
    }
    return requests.get( full_url, params=params )

def show_tool( tool_id ):
    full_url = BASE_URL + '/api/tools/' + tool_id

    params = {
        'key' : open( '.api-key' ).readline().strip(),
        'io_details' : True
    }
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = None
    if len( sys.argv ) == 1:
        response = list_tools()
    else:
        response = show_tool( sys.argv[1] )
    output.output_response( response )
