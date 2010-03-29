#!/usr/bin/python#ACS_ACU122.pyimport pcsc_readerimport thread,threadingfrom readerInfo import readerInfofrom Mifare_Ultralight import Mifare_Ultralightfrom Mifare_1K import Mifare_1Kfrom Mifare_4K import Mifare_4K#libraries for testing reasonfrom smartcard.System import *from smartcard.util import *import timeclass ACS_ACU122(pcsc_reader.PCSC_Reader):     def __init__(self,reader):         pcsc_reader.PCSC_Reader.__init__(self,reader)         self.reader = reader         self.readerInfo = readerInfo(reader.name,self.readername,self.hardware,self.supportProtocols,self.supportTagTypes)         self.connection = self.getConnectionToTag(reader)         self.connect(self.connection)         #set retry time to 1         self.doTransmition(self.connection,self.commandSet['setRetryTime'])     #parameters of touchatag     readername = 'ACS ACR 122U'     hardware = 'PN531'     supportProtocols = ('ISO14443A/B','ISO18092')     supportTagTypes = ('Mifare Ultralight','Mifare 1K','Mifare 4K')     #command sets     commandSet = {'setRetryTime':[0xFF,0x00,0x00,0x00,0x06,0xD4,0x32,0x05,0x00,0x00,0x00],                   'pollingCommand':[0xFF,0x00,0x00,0x00,0x04,0xD4,0x4A,0x01,0x00],                   'getResponse':[0xFF,0xC0,0x00,0x00]}     #runtime variable     tagType = None     tagUID = None     tagConnect = False     tagRelease = False     hasTagConnected = False     def isTagConnected(self):           if self.tagConnect:                 self.tagConnect = False                 self.hasTagConnected = True                 return True           else:                 return False     def isTagReleased(self):           if self.tagRelease:                 self.tagRelease = False                 self.hasTagConnected = False                 return True           else:                 return False     def update(self):         self.pollForATag()      def pollForATag(self):                    try:                   self.connect(self.connection)                   #???if OMNIKEY and touchatag are both connected                   #re-connect is needed for touchatag                                      data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])                   self.commandSet['getResponse'].append(trans2)                   result,get1,get2 = self.doTransmition(self.connection,self.commandSet['getResponse'])                   self.commandSet['getResponse'].pop()                   #operate the runtime variables according to the reponse of the direct transmit and get response data                   if hex(trans2) == '0x5':                      self.tagConnect = False                      if self.tagType == None:                         self.tagRelease = False                      else:                         self.tagRelease = True                         self.tagType = None                         self.tagUID = None                   elif hex(trans2) == '0xe':                         self.tagRelease = False                         if self.tagType == None:                            self.tagConnect = True                            self.tagUID = result[8:12]                            self.tagType = result[6]                         else:                            self.tagConnect = False                         #fake polling                         data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])                   elif hex(trans2) == '0x11':                         self.tagRelease = False                         if self.tagType == None:                            self.tagConnect = True                            self.tagUID = result[8:15]                            self.tagType = result[6]                         else:                            self.tagConnect = False                         #fake polling                         data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])                   else:                         pass          except:                   #User plug out reader when polling is executing                   pass     def getConnectedTag(self):         if hex(self.tagType) == '0x0':              return Mifare_Ultralight(toHexString(self.tagUID),self.reader.name)         elif hex(self.tagType) == '0x8':              return Mifare_1K(toHexString(self.tagUID),self.reader.name)         elif hex(self.tagType) == '0x18':              return Mifare_4K(toHexString(self.tagUID),self.reader.name)         else:              assert(1/0)     def getReaderInfo(self):         return self.readerInfo     def transmitAPDU(self,apdu):         self.connect(self.connection)         return self.doTransmition(self.connection,apdu)     def __del__(self):          pass#self-testingif __name__ == '__main__':       acs = ACS_ACU122(readers()[0])       while True:                 acs.pollForATag()                 if acs.isTagConnected():                     print acs.getConnectedTag().getTagInfo().getTagUID()                 if acs.isTagReleased():                     print "tag released!"