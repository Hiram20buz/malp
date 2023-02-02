# import required module
from cryptography.fernet import Fernet
import os

temp_dir =os.environ['TEMP']
arch1=f"{temp_dir}\ss1.png"

fernet = Fernet(b'abtIte6zsmWRVFkE8LZq06lxAx1kKRXTzm5L1c7BTQM=')


def enk():
    # opening the original file to encrypt
    with open(arch1, 'rb') as file:
        original = file.read()
         
    # encrypting the file
    encrypted = fernet.encrypt(original)
     
    # opening the file in write mode and
    # writing the encrypted data
    with open(arch1, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
