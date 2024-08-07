letter = input("Enter the data : ")
shift = 3
encrypt = ''
decrypt = ''

for char in letter:
    if(char.islower()):
        encrypt += chr((ord(char)+shift-97)% 26 + 97)
    elif(char.isupper()):
        encrypt += chr((ord(char)+shift-65)% 26 + 65)
    elif(char.isdigit()):
        encrypt += chr((ord(char)+shift-48)% 10 + 48)
    elif(char.isspace()):
        encrypt += ' '

print("Encrypted value:")
print(encrypt)

for char in encrypt:
    if(char.islower()):
        decrypt += chr((ord(char)-shift-97)% 26 + 97)
    elif(char.isupper()):
        decrypt += chr((ord(char)-shift-65)% 26 + 65)
    elif(char.isdigit()):
        decrypt += chr((ord(char)-shift-48)% 10 + 48)
    elif(char.isspace()):
        decrypt += ' '


print("Decrypted value:")
print(decrypt)
