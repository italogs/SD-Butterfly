# coding: latin-1
import socket
import math

def buscarId(enderecoClientes,enderecoOrigem):
	chave = 0;
	for item in enderecoClientes:
		if(item == enderecoOrigem):
			return chave;
		chave = chave + 1;

HOST = socket.gethostbyname(socket.gethostname());
PORT = 5000;
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
orig = (HOST, PORT);
udp.bind(orig);
id = 0;



print 'Programa Somador de 0 ate N - Utilizando Algoritmo BUTTERFLY\n\n'
print 'Entre com o numero de processadores que vao se conectar';
N = int(raw_input());
N = N + 1;#SOMANDO MAIS 1 COM O MESTRE
nummsg = math.log(N,2);


conectados = 0;
enderecoClientes = [];
enderecoClientes.append(orig);
print 'Aguardando conexoes...';
while conectados < int(N) - 1:
	mensagem, enderecoCliente = udp.recvfrom(1024);
	enderecoClientes.append(enderecoCliente);
	conectados = conectados + 1;
	print conectados,' conectados';
print 'Clientes conectados com sucesso...\nID ',id,' registrado.\n\n';

print 'Entre com o numero a ser feito o seu somatorio';
numero = int(raw_input());

concatlistClients = [];
for i in enderecoClientes:
	concatlistClients.append(str(i[1]));
concatText = "-".join(concatlistClients);

i = 1;
while  i <= N - 1:
	udp.sendto (str(i), enderecoClientes[i]);
	udp.sendto (str(numero), enderecoClientes[i]);
	udp.sendto (str(N), enderecoClientes[i]);
	udp.sendto (str(concatText), enderecoClientes[i]);
	i = i + 1;

somatorio =0;
parcela = int(int(numero)/N);
inicio = parcela * id ;
fim = (parcela * id ) +1;
i = inicio;
while i <= fim:
	somatorio = somatorio + i;
	i = i + 1;

cont = 0;
idrec = N/2;
while True:
	somapar, enderecoOrigem = udp.recvfrom(1024);
	print 'Recebeu de ID: ',buscarId(enderecoClientes,enderecoOrigem);
	somatorio = somatorio + int(somapar);
	idrec = idrec / 2;
	cont = cont + 1;
	if(cont >= nummsg):
		break;
	
print 'Resultado:',somatorio,'\n\n';
print 'Fim do programa.';

