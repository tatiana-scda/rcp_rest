#!/users/zireael/anaconda3/bin/python

#./server port Netfile Ixfile Netixlanfile
#Onde [port] é o porto no qual o servidor receberá mensagens, [Netfile] é o caminho do arquivo
#de redes, [Ixfile] é o caminho do arquivo de IXPs e [Netixlanfile] é o caminho do arquivo de
#associações.

from flask import Flask
import sys, json

port           = sys.argv[1]
netfile        = sys.argv[2]
ixfile         = sys.argv[3]
netixlanfile   = sys.argv[4]

app = Flask(__name__)

# test endpoint
@app.route('/')
def hello_world():
    return 'Run Forest, run! Just kidding, API is working'

# endpoints

@app.route('/api/ixids')
def ixids():
# resp: {"data": <lista dos identificadores dos IXPs>}
    return '/api/ixids'

@app.route('/api/ixnets/{ix_id}')
def ix_id():
# resp: {"data": <lista dos identificadores das redes do IXP identificado por 'ix_id'>}
    return '/api/ixids'

@app.route('/api/netname/{net_id}')
def net_id():
 
# resp: {"data": <nome da rede identificada por 'net_id'>}
    return '/api/ixids'