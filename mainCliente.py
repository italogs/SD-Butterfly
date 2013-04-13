# coding: latin-1
# Escravo (ID!=0)

# Inicio
#   Receba (numero de elemento(0));

# 	Constructor  
#   somapar=0;
#   parcela = (int)numero/N;
#   inicio = parcela*ID;
#   fim = (parcela*ID)+1;

#	doSum
#   para i=inicio até fim faça
#     somapar=somapar+i;
#   fim para

# 	ReceiveSendSum
#   metade=N;
#   repita
#     metade=metade/2;
#     somatorio=somapar;
#     se id >= metade entao
#       EnviE (somapar para elemento (id-metade));
#     senao
#      se id!=0 entao
#       Receba (somapar de elemento (id+metade)); 
#       somatorio=somatorio+somapar;
#       somapar=somatorio;
#      fimse
#     fimse  
#   enquanto id < metade;
# FIM
import socket
import math
import cliente

HOST = 'localhost';
PORT = 5000;
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
dest = (HOST, PORT);
udp.sendto ('Conectado com Sucesso', dest);
serverAdress = [];
print 'Aguardando resposta do servidor....';
id, serverAdress = udp.recvfrom(1024);
number, serverAdress = udp.recvfrom(1024);
nProcessors, serverAdress = udp.recvfrom(1024);
listClients, serverAdress = udp.recvfrom(1024);


print 'id',id;
print 'number',number;
print 'nProcessors',nProcessors;
print 'serverAdress',serverAdress;
print 'listClients',listClients;

listClients = listClients.split('-');
c = cliente.Client(int(id),number,nProcessors);
c.doSelfSum();
c.receiveSendSum(udp,serverAdress,listClients,HOST);
print 'fim programa';