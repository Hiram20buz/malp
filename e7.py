# import required module
from cryptography.fernet import Fernet

fernet = Fernet(b'abtIte6zsmWRVFkE8LZq06lxAx1kKRXTzm5L1c7BTQM=')
 

 
# opening the encrypted file
with open('ss1.png', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('ss1.png', 'wb') as dec_file:
    dec_file.write(decrypted)
