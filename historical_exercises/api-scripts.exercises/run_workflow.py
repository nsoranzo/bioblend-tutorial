#!/usr/bin/env python

import sys
import json
import output
import requests

BASE_URL = 'http://localhost:8080'

# -----------------------------------------------------------------------------
def run_workflow( workflow_id, history_id, source_step, hda_id ):
    # http://galaxy-central.readthedocs.org/en/latest/lib/galaxy.webapps.galaxy.api.html#galaxy.webapps.galaxy.api.workflows.WorkflowsAPIController.create
    # lib/galaxy/webapps/galaxy/api/workflows.py, def create
    full_url = BASE_URL + '/api/workflows'

    # dataset (ds) map/dictionary letting the workflow know which datasets to use for inputs
    #   mapping a workflow step (source_step) to a dataset (in our case, an hda with the given
    #   id). Note: 'src' can also be a library dataset (ldda)
    ds_map = {}
    #EXERCISE: fill out ds_map with source_step and hda_id

    # if our workflow had more than one input, we could continue adding source_steps and datasets
    #   for each input required

    # NOTE: that the workflow must be well formed: i.e. it must have input steps

    data = {
        'key'           : open( '.api-key' ).readline().strip(),
        'workflow_id'   : workflow_id,
        # we always need a target history - for input datasets and output.
        #   GOTCHA: In the case of this API call, the history id requires a prefix of 'hist_id='
        'history'       : 'hist_id=' + history_id,
        # sub-objects in POST data often needs to be encoded as a json string
        'ds_map'        : json.dumps( ds_map )
    }
    #EXERCISE: ...


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    workflow_id, history_id, source_step, hda_id = sys.argv[1:5]
    response = run_workflow( workflow_id, history_id, source_step, hda_id )
    output.output_response( response )
