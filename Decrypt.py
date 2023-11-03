import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file == "Encrypt.py" or file == "lockKey.key" or file=="Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)
# Let's Decrypt the files using cryptography library

with open("lockKey.key", "rb") as key:
    secretkey = key.read()
    
secret_phrase = "Team"

user_phrase =input("Enter the secret phrase to decrypt\n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, 'rb') as lockKey:
            contents=lockKey.read()
        decrypted_content = Fernet(secretkey).decrypt(contents)
        with open(file, 'wb') as lockKey:
            lockKey.write(decrypted_content)
    print("Congrats! You have successfully decrypted your files.\n")
else:
    print("Sorry! Wrong secret phrase . Can't decrypt!\n")    