import os
import pyaes

# abre o arquivo criptografado
file_name = "teste.txt.cryptografado"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remove o arquivo criptografado
os.remove(file_name)

# criar o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()