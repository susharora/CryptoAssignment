import hashlib
def Mac_Generate(key,message):
    key = str(key)
    MacInput = message + key
    MacInputEncode = MacInput.encode()
    HashObj = hashlib.sha256(MacInputEncode)
    HashHex = HashObj.hexdigest()
    return(HashHex)
Msg01 = "This is the first message"
Key01 = 123
#key = input("Enter Key:")
MacGenerated = Mac_Generate(Key01,Msg01)
MacExpected = "7a6ae08da05ae5b291266afc65a65c6f3551a31570c4636ed17733f9783fdd1e"

print('Mac generated-',MacGenerated)
print('Mac Expected-',MacExpected)
if (MacGenerated == MacExpected):
    print ('Ok')
else:
    print ('Bad')
