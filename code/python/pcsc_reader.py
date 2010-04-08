#!/usr/bin/python#pcsc_reader.pyfrom smartcard.System import *from smartcard.util import *from smartcard.CardRequest import CardRequestfrom smartcard.CardType import AnyCardType,ATRCardType,CardTypefrom UnknownTag import UnknownTagfrom database import *import smartcardfrom readerInfo import readerInfoimport readerfrom ui import userInterfaceimport stringclass readerBasedCardType(CardType):         def __init__(self,focusReader):             self.focusReader = focusReader                      def matches(self,atr,reader):               if string.find(reader.name,self.focusReader) == 0:                   return Trueclass PCSC_Reader(reader.abstractReader):   def __init__(self,pcsc_reader):       reader.abstractReader.__init__(self)       self.pcsc_reader = pcsc_reader   #tag status   hasAnOldTag = False   tagTouched = False   tagRemoved = False   atr = None   def isTagConnected(self):         if self.tagTouched:               self.tagTouched = False               self.hasAnOldTag = True               return True         else:               return False   def isTagReleased(self):         if self.tagRemoved:               self.tagRemoved = False               self.hasAnOldTag = False               return True         else:               return False   def update(self):               state = self.pollForATag()               #update tagTouched,tagRemoved               if self.hasAnOldTag:                    if state:                           self.tagTouched = False                           self.tagRemoved = False                    else:                           self.tagTouched = False                           self.tagRemoved = True               else:                    if state:                           self.tagTouched = True                           self.tagRemoved = False                    else:                           self.tagTouched = False                           self.tagRemoved = False                              def getConnectedTag(self):       return  UnknownTag('Unknown',self.pcsc_reader.name)   def getConnectionToTag(self,reader):       return reader.createConnection()   def connect(self,connection):           connection.connect()   def doTransmition(self,connection,commandSet, protocol):       data,sw1,sw2 =  connection.transmit(commandSet,protocol)       return data,sw1,sw2   #universal polling function(can be overwritten for specified kind of readers.(eg.TouchaTag)   def pollForATag(self):       cardtype =readerBasedCardType(self.pcsc_reader.name)       cardrequest = CardRequest(timeout = 0,cardType=cardtype)       try:           cardservice = cardrequest.waitforcard()           cardservice.connection.connect()           self.atr = cardservice.connection.getATR()           return True       except:           return False   def disconnect(self,connection):       connection.disconnect()   def enterAPDU(self):       pass   def getATR(self):       return toHexString(self.atr)   def backToNormal(self):       pass         def getReaderInfo(self):       return readerInfo(self.pcsc_reader.name,UNKNOWN,UNKNOWN,None,None)