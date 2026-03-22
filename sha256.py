import hashlib
#Msg = input("enter input for hashing:")
Msg = "Sam is ok and so is Jane"
MsgBytes = Msg.encode()
Hash = hashlib.sha256(MsgBytes)
HashHex = Hash.hexdigest()
HashInput = input("Enter expected hash value:")
if (HashInput == HashHex):
    print('They match')
else:
    print('Do not match')


