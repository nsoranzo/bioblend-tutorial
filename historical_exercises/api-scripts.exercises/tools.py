#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def list_tools():
    #EXERCISE: build params and include  'in_panel' : False
    return requests.get( full_url, params=params )

def show_tool( tool_id ):
    #EXERCISE: build params, including 'io_details' : True, and request


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    response = None
    # if passed an id, show details for that; if no id: return info for all tools
    if len( sys.argv ) == 1:
        response = list_tools()
    else:
        response = show_tool( sys.argv[1] )
    output.output_response( response )
