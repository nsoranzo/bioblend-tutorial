#!/usr/bin/env python

import sys
import json
import requests
import output

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def run_tool( tool_id, history_id, **kwargs ):
    full_url = BASE_URL + '/api/tools'

    #EXERCISE: POST...

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # e.g. ./run_tool.py Filter1 ebfb8f50c6abde6d '{ "input" : { "src": "hda", "id": "77f74776fd03cbc5" }, "cond" : "c6>=100.0" }'
    # e.g. ./run_tool.py sort1 f597429621d6eb2b '{ "input": { "src": "hda", "id": "b472e2eb553fa0d1" }, "column": "c6", "style": "alpha", "column_set_0|other_column" : "c2", "column_set_0|other_style": "num" }'
    tool_id, history_id = sys.argv[1:3]
    params = json.loads( sys.argv[3] ) if len( sys.argv ) >= 4 else {}
    response = run_tool( tool_id, history_id, **params )
    output.output_response( response )
