#!/users/zireael/anaconda3/bin/python
# -*- coding: utf-8 -*-

# #!/usr/bin/python

from __future__ import print_function
import socket, json, sys

# python client.py IP:port analysis

ip_port       = sys.argv[1]
analysis      = sys.argv[2]

HOST = ip_port[0:ip_port.find(':')]
PORT = int(ip_port[ip_port.find(':')+1:])

def err_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def data_setting (endpoint, ip, port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((ip, port))

    get = 'GET ' + endpoint + ' HTTP/1.1\nHost:' + ip + '\n\n'
    tcp.sendall(get.encode('utf8'))
    answer = recv_json(tcp)

    tcp.close()
    return answer

def recv_json(sock):
    answer = b''
    response = True
    while response != b'':
        response = sock.recv(1024)
        answer += response
        #print(b'antes do loads'+answer)
    answer_body = answer[answer.find(b'{'):]    
    return json.loads(answer_body)
        
if __name__ == "__main__":
    if analysis == '0':
        ixs_by_network = {}
        
        ixs = data_setting('/api/ix', HOST, PORT)
        for ix in ixs['data']:
            ixnets = data_setting('/api/ixnets/' + str(ix['id']), HOST, PORT)
            for ixnet in ixnets['data']:
                if ixnet in ixs_by_network:
                    ixs_by_network[ixnet] += 1
                else:
                    ixs_by_network[ixnet] = 0
        
        for net in ixs_by_network:
            network_name = data_setting('/api/netname/' + str(net), HOST, PORT)

            print(str(net) + '\t' + network_name['data'] + '\t' + str(ixs_by_network[net]))

    elif analysis == '1':
        ixs = data_setting('/api/ix', HOST, PORT)
        for ix in ixs['data']:
            ixnets = data_setting('/api/ixnets/'+ str(ix['id']), HOST, PORT)
            size = len(ixnets['data'])
            print(str(ix['id']) + '\t' + ix['name'] + '\t' + str(size))