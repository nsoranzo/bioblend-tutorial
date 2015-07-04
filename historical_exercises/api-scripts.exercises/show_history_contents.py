#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
# http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.history_contents.HistoryContentsController.show
# lib/galaxy/webapps/galaxy/api/history_contents.py, def index
def show_history_contents( history_id, contents_id ):
    # even further specify a resource by using the URL - this time telling the
    #   API to look for a specific element (contents_id) in a specific history
    full_url = #... 


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    history_id, contents_id = sys.argv[1:3]
    response = show_history_contents( history_id, contents_id )
    output.output_response( response )
