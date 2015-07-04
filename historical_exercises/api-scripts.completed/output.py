#!/usr/bin/env python
"""
Format output.
"""

import json

def pformat_as_json( data ):
    return json.dumps( data, indent=2, sort_keys=True, separators=( ',', ': ' ) )

def pprint_as_json( data ):
    print pformat_as_json( data )

def output_response( response ):
    try:
        pprint_as_json( response.json() )
    except Exception, e:
        if response is not None:
            print response.text
        else:
            raise
