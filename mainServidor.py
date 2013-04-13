# coding: latin-1
# ESTE SOMATORIO SUPOEM QUE O NUMERO DE ELEMENTOS É 
# POTENCIA DE 2 - SOMATÓRIO BUTTERFLY
# N é o número de elementos processadores

# Mestre (ID == 0)

# Inicio
#   nummsg=log2(N);
#   Leia(numero);

#   sendNumberToSlaves
#   para i=1 até N-1 faça
#     Envie (numero para elemento (i));
#   fim para

#   doSelfSum
#   somatorio=0;
#   parcela = (int)numero/N;
#   inicio = parcela*ID;
#   fim = (parcela*ID)+1;
#   para i=inicio até fim faça
#      somatorio=somatorio+i;
#   fim para

#	receiveSum
#   cont=0;
#   idrec=N/2;
#   repita
#     Receba (somapar de elemento(idrec));
#     somatorio=somatorio+somapar;
#     idrec=idrec/2;
#     cont=cont+1;
#   enquanto cont<=nummsg;

#   escreva(somatorio);
# FIM
import servidor
import socket
import math

HOST = 'localhost';
PORT = 5000;
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
orig = (HOST, PORT);
udp.bind(orig);

print 'Programa Somador de 0 ate N - Utilizando Algoritmo BUTTERFLY\n\n'

print 'Digite a quantidade de clientes que sao esperados:\n'
#nProcessors = int(raw_input());
nProcessors = 3;

print 'Aguardando ',nProcessors,' clientes';
conected = 0;
listClients = [];
while conected < int(nProcessors):
    message, adressClient = udp.recvfrom(1024)
    print message,adressClient,conected;
    listClients.append(adressClient)
    conected = conected + 1

print 'Entre com o numero a ser feito o seu somatorio\n'
#number = int(raw_input());
number = 4000;

s = servidor.Server(nProcessors,number,listClients);
s.concatAdress();
s.sendNumberToSlaves(udp);
s.doSelfSum();
s.receiveSum(udp);

print 'Result:',s.getSum();