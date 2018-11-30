#!/users/zireael/anaconda3/bin/python

import socket, json

# ./client IP:port Opt

#Análise 0 (IXPs por rede)
#Para essa análise o cliente deve produzir na saída padrão um TSV UTF-8 (tabelas com células separadas por tabulações '\t') com uma rede por linha, contendo as seguintes colunas (nessa ordem):''
# Identificador da rede: esse dado pode ser encontrado no campo id do arquivo net.json; ou no campo net_id do arquivo netixlan.json
# Nome da rede: esse dado pode ser encontrado no campo name do arquivo net.json
# Número de IXPs associados à rede: deve ser gerado pelo seu cliente
#id ou net_id name IXPassociate

# Análise 1 (redes por IXP)
# Para essa análise o cliente deve produzir na saída padrão um TSV UTF-8 (tabelas com células separadas por tabulações '\t') com uma rede por linha, contendo as seguintes colunas (nessa ordem):
# Identificador do IXP: esse dado pode ser encontrado no campo id do arquivo ix.json; ou no campo ix_id do arquivo netixlan.json
# Nome do IXP: esse dado pode ser encontrado no campo name do arquivo ix.json
# Número de redes associadas ao IXP: deve ser gerado pelo seu cliente

ip_port       = sys.argv[1]
analysis      = sys.argv[2]
tcp           = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ip_port[0:ip_port.find(':')]
PORT = int(ip_port[ip_port.find(':')+1:])