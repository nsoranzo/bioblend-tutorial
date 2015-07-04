#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def dataset_download( id, filepath=None ):
    full_url = BASE_URL + '/datasets/' + id + '/display'

    params = {
        'key'           : open( '.api-key' ).readline().strip()
    }
    response = requests.get( full_url, params=params )
    if not response or response.status_code != 200:
        raise Exception( 'Dataset display failed: %s, %s' %
            ( id, str( response.text if response else None ) ) )

    if filepath:
        with open( filepath, 'w' ) as outfile:
            outfile.write( response.text )
    else:
        print response.text
    return response


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    id, filepath = sys.argv[1:3]
    dataset_download( id, filepath )
