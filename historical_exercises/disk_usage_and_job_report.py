#!/usr/bin/env python


import sys
import json
import yaml
import requests

BASE_GALAXY_URL = 'http://localhost:8080'
API_KEY = '225960e27cf51d0a012755a5db11cee1'

users = requests.get("%s/api/users?key=%s" % (BASE_GALAXY_URL, API_KEY)).json()

# We have a dictionary of users.

for user in users:
    user_details = requests.get("%s/api/users/%s?key=%s" % (BASE_GALAXY_URL, user['id'], API_KEY))
    print user_details.json()

    # We must now impersonate this user, because a user can only query their
    # own jobs

    user_jobs = requests.get("%s/api/jobs?key=%s&run_as=%s" % (BASE_GALAXY_URL, API_KEY, user['id'])).json()
    print len(user_jobs)
