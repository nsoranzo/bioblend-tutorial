#!/usr/bin/env python
#
# quick and dirty script to install repositories from the toolshed at their
# newest installable revisions.
#
# Sample invocation:   python install_toolshed_yaml.py tools.yaml MASTERLOCK http://localhost:8080
# yaml format is:
#
# <shed>:
#   <owner>:
#   - <repo>
#   - <repo>
#
# e.g.:
#
# toolshed.g2.bx.psu.edu:
#   devteam:
#   - bam_to_sam
#   - ctd_batch
#


import sys
import json
import yaml
import requests

BASE_GALAXY_URL = 'http://localhost:8080'

try:
    yamldata = yaml.load( open( sys.argv[1] ) )
    key = sys.argv[2]
except:
    print >>sys.stderr, 'usage: %s <repos yaml> <galaxy api key> <galaxy url>' % sys.argv[0]
    raise

for shed, owners in yamldata.items():
    for owner, names in owners.items():
        for name in names:
            print "Handling repository %s:%s:%s" % (shed, name, owner)
            # Get the latest installable revision of this repository directly
            # from the toolshed.  This call is a GET to something like:
            # GET https://toolshed.g2.bx.psu.edu/api/repositories/get_ordered_installable_revisions
            # with GET args 'name' and 'owner'

            url = 'https://%s/api/repositories/get_ordered_installable_revisions?name=%s&owner=%s' % ( shed, name, owner )
            response = requests.get(url)
            # The response from the toolshed should be something like the following list, which is valid JSON:
            # ["dc20f447c0e2", "250151b4d934"]
            # In this list, the last item is the most recent tool version
            rev = response.json()[-1]
            data = {'key': key,
                    'tool_shed_url': 'https://%s' % shed,
                    'name': name,
                    'owner': owner,
                    'changeset_revision': str(rev),
                    'install_repository_dependencies': True,
                    'install_tool_dependencies': True }
            url = '%s/api/tool_shed_repositories/new/install_repository_revision?key=%s' % ( BASE_GALAXY_URL, key )
            headers = { 'Content-Type': 'application/json' }
            response = requests.post(url,
                                     data=json.dumps(data),
                                     headers=headers)
            #  Bonus points here for actually inspecting the response and
            #  printing something appropriate
            print response.text
