#!/usr/bin/env python

import sys
import os
import json
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def create_user( username, email, password ):
    full_url = BASE_URL + '/api/users'

    data = {
        'key'           : 'MASTERLOCK',
        'username'      : username,
        'email'         : email,
        'password'      : password
    }
    return requests.post( full_url, data=data )


# -----------------------------------------------------------------------------
def create_quota( name, description, user_id, amount ):
    full_url = BASE_URL + '/api/quotas'

    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        'name'          : name,
        'description'   : description,
        'operation'     : '=',
        'amount'        : amount,
        'default'       : 'no',
        'in_users'      : user_id
    }
    return requests.post( full_url, data=data )


# -----------------------------------------------------------------------------
def create_history_as_another_user( user_id, name ):
    full_url = BASE_URL + '/api/histories'
    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        'run_as'        : user_id,
        'name'          : name
    }
    return requests.post( full_url, data=data )


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
        'run_as'        : user_id
    }

    response = None
    with open( filepath, 'rb' ) as file_to_upload:
        files = { 'files_0|file_data' : file_to_upload }
        response = requests.post( full_url, data=data, files=files )
    return response


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    username, email, password = sys.argv[1:4]
    # create user
    response = create_user( username, email, password )
    user_data = response.json()
    user_id = user_data[ 'id' ]

    response = create_quota( 'individual quota', 'default new user quota', user_id, '20gb' )
    response = create_history_as_another_user( user_id, 'starter history' )
    history_data = response.json()
    history_id = history_data[ 'id' ]

    response = upload_file_as_another_user( user_id, history_id, 'data/5.bed' )
    print user_data
