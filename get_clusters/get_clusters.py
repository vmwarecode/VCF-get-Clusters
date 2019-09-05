#Get all Clusters
import requests
import json
import sys

def get_help():
    help_description = '''\n\t\t----Get Clusters----
    Usage:
    python get_clusters.py <hostname> <username> <password>\n Refer to documentation for more detais\n'''
    print help_description

def get_domains():
    arguments = sys.argv
    if(len(arguments) < 3):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    password = arguments[3]
    headers = {'Content-Type': 'application/json'}
    url = hostname+'/v1/clusters/'
    response = requests.get(url, headers=headers,auth=(username, password))
    if(response.status_code == 200):
        response = json.loads(response.text)
        print json.dumps(response,indent=4, sort_keys=True)
    else:
        print "Error reaching the server."
        print response.text
        exit(1)
get_domains()
