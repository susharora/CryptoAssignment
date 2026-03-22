import hashlib
Msg01 = "This is the first message"
Msg02 = "This is the first message1"

MsgEnc01 = Msg01.encode()
MsgEnc02 = Msg02.encode()

HashObj01 = hashlib.md5(MsgEnc01)
HashObj02 = hashlib.md5(MsgEnc02)
HashObjHex01 = HashObj01.hexdigest()
HashObjHex02 = HashObj02.hexdigest()
print (HashObjHex01) 
print(HashObjHex02)
