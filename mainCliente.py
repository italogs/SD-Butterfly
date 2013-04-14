# coding: latin-1
import socket
import math


def buscarId(enderecoClientes,enderecoOrigem):
	chave = 0;
	for item in enderecoClientes:
		if(item == enderecoOrigem):
			return chave;
		chave = chave + 1;
	return -1;


HOST = '127.0.0.1';
PORT = 5000;
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
dest = (HOST, PORT);
udp.sendto ('Conectado com Sucesso', dest);
serverAdress = [];
print 'Aguardando resposta do servidor....';
id, serverAdress = udp.recvfrom(1024);
id = int(id);


numero, serverAdress = udp.recvfrom(1024);
N, serverAdress = udp.recvfrom(1024);
concatListClients, serverAdress = udp.recvfrom(1024);


numero = int(numero);
N = int(N);


enderecoClientes = [];

concatListClients = concatListClients.split('-');
for i in concatListClients:
	enderecoClientes.append((HOST,int(i)));
print 'Meus detalhes:';
print 'ID: ',id;
print 'Endereco',enderecoClientes[id];


somapar = 0;
parcela = int(numero/N);
inicio = parcela * id ;
fim = (parcela * id) + 1;

i = inicio;
while i <= fim:
	somapar = somapar + i;
	i = i + 1;

metade = N;
while True:
	metade = int(metade / 2);
	somatorio = somapar;
	if(id >= metade):
		idEnviar = int(id - int(metade));
		print 'Enviou para ID: ',idEnviar;
		udp.sendto (str(somapar), enderecoClientes[idEnviar]);
	else:
		if(id != 0):
			somapar, enderecoOrigem = udp.recvfrom(1024);
			print 'Recebeu de ID: ',buscarId(enderecoClientes,enderecoOrigem);
			somatorio = somatorio + int(somapar);
			somapar = somatorio;
	if(id >= metade):
		break;

print 'Processador encerrado.';

