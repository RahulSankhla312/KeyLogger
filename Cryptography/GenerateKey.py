from cryptography.fernet import Fernet

key = Fernet.generate_key()  # generate a key
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()
