#!/usr/bin/python
#database.py


#-------------------------------------------------------------------------------
#UNKNOWN TYPE-------------------------------------------------------------------
#-------------------------------------------------------------------------------
UNKNOWN = 'Unknown'

#-------------------------------------------------------------------------------
#readerTypes--------------------------------------------------------------------
#-------------------------------------------------------------------------------
readerTypes = (TOUCHATAG,OMNIKEY_CARDMAN_5321) = ('TOUCHATAG','OMNIKEY_CARDMAN_5321')


#-------------------------------------------------------------------------------
#tagTypes-----------------------------------------------------------------------
#-------------------------------------------------------------------------------
tagTypes = (MIFARE_ULTRALIGHT,
            MIFARE_1K,
            MIFARE_4K,
            TAGIT) = ('MIFARE_ULTRALIGHT','MIFARE_1K','MIFARE_4K','TAGIT')
#-------------------------------------------------------------------------------
#SAK Byte
#-------------------------------------------------------------------------------
SAK = {MIFARE_ULTRALIGHT:'0x0',
       MIFARE_1K:        '0x8',
       #'Mifare_MINI':      '0x9',
       MIFARE_4K:       '0x18'
       #'Mifare_Desfire':  '0x20',
       #'JCOP30':          '0x28',
       #'Gemplus MPCOS':   '0x98'
       }
#-------------------------------------------------------------------------------
#NN Byte
#-------------------------------------------------------------------------------
NN = {MIFARE_ULTRALIGHT:'0x3',
      MIFARE_1K        :'0x1',
      MIFARE_4K        :'0x2'}

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
RFIDProtocols = (ISO14443,ISO18092,ISO15693) = ('ISO14443A/B','ISO18092','ISO15693')

#-------------------------------------------------------------------------------
Hardware = (PN531,PN532,PN533) = ('PN531','PN532','PN533')

#-------------------------------------------------------------------------------
externalTools = (CARDSELECT,ISOTYPE,READMIFARE1K,READMIFAREULTRA,READMIFARESIMPLE) = range(5)

