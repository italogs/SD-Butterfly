# coding: latin-1
class Client(object):

  id,sum,sumAux,part,start,fim,number,nProcessors = 0,0,0,0,0,0,0,0;

  def __init__(self,id,number,nProcessors):
    self.id = int(id);
    self.number = int(number);
    self.nProcessors = int(nProcessors);

  def doSelfSum(self):
    self.sumAux = 0;
    self.part = int(self.number/self.nProcessors);
    self.start = self.part * self.id;
    self.end = self.start + 1;
    for i in range(self.start,self.end + 1):
      self.sumAux = self.sumAux + i;

  def receiveSendSum(self,udp,serverAdress,listClients,HOST):
    half = self.nProcessors;
    while True:
      half = half / 2;
      self.sum = self.sumAux;
      if(int(self.id) >= int(half)):
        #       EnviE (somapar para elemento (id-metade));
        udp.sendto (str(self.sumAux), (HOST,int(listClients[self.id - half ])));
      elif (int(self.id) != 0):
        sumTemp, serverAdress = udp.recvfrom(1024);
        self.sumAux = int(sumTemp);
        #Receba (somapar de elemento (id+metade));
        self.sum = self.sum + self.sumAux;
        self.sumAux = self.sum;
      if(int(self.id) >= int(half)):
        break;