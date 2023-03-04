#   From geeksforgeeks.org

#
#   Encrypt
#

# import required module
from cryptography.fernet import Fernet
import os
import glob
import sys
# key generation
key = Fernet.generate_key()

from pathlib import Path

mydir = Path("mel")
for filename in glob.iglob('C:/Users/bakra/Desktop/encrypted-files/mel/**/*.*', 
                   recursive = True):
    print(filename)
    # do your stuff


# string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

# opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
 
# using the generated key
    fernet = Fernet(key)
 
# opening the original file to encrypt
    with open(filename, 'rb') as file:
        original = file.read()
     
# encrypting the file
    encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

#
#   pause
#

decrypting = input("Continue to decryption? ")

if(decrypting == "no"):
    sys.exit("1")

#
#   Decrypt
#



# using the key
fernet = Fernet(key)

for filename in glob.iglob('C:/Users/bakra/Desktop/encrypted-files/mel/**/*.*', 
                   recursive = True):
    print(filename)
    # do your stuff

# opening the encrypted file
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
 
# decrypting the file
    decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)