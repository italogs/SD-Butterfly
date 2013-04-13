# coding: latin-1
import socket
import math
import servidor

class Server(object):
  nProcessors,nMessages,id,number,sum,part,start,end,listClients,concatlistClients = 0,0,0,0,0,0,0,0,None,None;

  def getSum(self):
    return self.sum;

  def doSelfSum(self):
    self.sum = 0;
    self.part = int(self.number/self.nProcessors);
    self.start = self.part * self.id;
    self.end = self.start + 1;

    for i in range(self.start,self.end+1):
      self.sum = self.sum + i;

  def receiveSum(self,udp):
    count = 0;
    idRec = self.nProcessors/2;
    while True:
      sumTemp, serverAdress = udp.recvfrom(1024);
      #     Receba (somapar de elemento(idrec));
      somapar = int(sumTemp);
      self.sum = self.sum + somapar;
      idRec = idRec/2;
      count = count + 1;
      if(count > self.nMessages):
        break;

  def __init__(self,nProcessors,number,listClients):#Constructor
    self.nProcessors = int(nProcessors);
    self.number = int(number);
    self.nMessages = math.log(float(self.nProcessors),2);
    self.listClients = listClients;

  def sendNumberToSlaves(self,udp):
    for novoId in range(0,self.nProcessors):
      udp.sendto (str(novoId), self.listClients[novoId]);
      udp.sendto (str(self.number), self.listClients[novoId]);
      udp.sendto (str(self.nProcessors), self.listClients[novoId]);
      concatText = "-".join(self.concatlistClients);
      udp.sendto (str(concatText), self.listClients[novoId]);

  def concatAdress(self):
    temp = [];
    for client in self.listClients:
      temp.append(str(client[1]));
    self.concatlistClients = temp;




