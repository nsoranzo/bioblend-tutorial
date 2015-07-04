#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def args_to_dict( *args ):
    keys = [ arg for i, arg in enumerate( args ) if i % 2 == 0 ]
    vals = [ arg for i, arg in enumerate( args ) if i % 2 == 1 ]
    return dict( zip( keys, vals ) )

def dataset_data( id, **extra_params ):
    full_url = BASE_URL + '/api/datasets/' + id

    params = {
        'key'           : open( '.api-key' ).readline().strip(),
    }
    if extra_params:
        params.update( extra_params )
    return requests.get( full_url, params=params )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # e.g. ./dataset_data.py bf60fd5f5f7f44bf data_type raw_data provider line
    # e.g. ./dataset_data.py 77f74776fd03cbc5 data_type raw_data provider dict column_names chr,start,stop,name,strand,length limit 5 offset 3
    extra_params = args_to_dict( *sys.argv[2:] )
    response = dataset_data( sys.argv[1], **extra_params )
    #output.output_response( response )

    provider = extra_params.get( 'provider', None )
    if provider in ( 'line', 'regex-line' ):
        for datum in response.json()[ 'data' ]:
            print datum
    elif provider in ( 'column', 'dict' ):
        output.pprint_as_json( response.json()[ 'data' ] )
    elif provider:
        output.pprint_as_json( response.json() )
