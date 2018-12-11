#!/usr/bin/python
# -*- coding: utf-8 -*-

# #!/users/zireael/anaconda3/bin/python

from flask import Flask
import sys, json

port           = sys.argv[1]
netfile        = sys.argv[2]
ixfile         = sys.argv[3]
netixlanfile   = sys.argv[4]

app = Flask(__name__)

# test endpoint
@app.route('/42')
def hello_world():
    return 'The answer to the ultimate question of life, the Universe, and everything is ' + str(ord('*'))

# endpoints
@app.route('/api/ix')
def ix():
    with open(ixfile) as ix:
        ix_file = json.load(ix)
        ix_data = ix_file['data']
    return json.dumps({"data": ix_data})

@app.route('/api/ixnets/<ix_id>')
def ixnets(ix_id):
    with open(netixlanfile) as netix:
        netixlan_file = json.load(netix)
        all_net_ids   = []
        for net in netixlan_file['data']:
            if net['ix_id'] == int(ix_id):
                if(net['net_id'] not in all_net_ids):
                    all_net_ids.append(net['net_id'])
    return json.dumps({"data": all_net_ids})

@app.route('/api/netname/<net_id>')
def netname(net_id):
    with open(netfile) as nets:
        net_file = json.load(nets)
        for net in net_file['data']:
            if net['id'] == int(net_id):
                return json.dumps({"data": net['name']})

app.run(host='0.0.0.0', port=port)