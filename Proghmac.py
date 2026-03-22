import hashlib
import hmac
Msg01 = "This is the first message"
Key01 = 123
MsgEnc01 = Msg01.encode()
KeyEnc01 = str(Key01).encode()
HmacObj = hmac.new(KeyEnc01,MsgEnc01,hashlib.sha256)
MacGenerated = HmacObj.hexdigest()
MacExpected = "dd748b818a3fc106b6dbf7a73919d94d6bb242663839342972d56ee8a82708d2"
#MacExpected = MacExpected.encode()
print('Mac generated-',MacGenerated)
print('Mac Expected-',MacExpected)
if (MacGenerated == MacExpected):
    print ('Ok')
else:
    print ('Bad')
