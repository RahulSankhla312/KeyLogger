from cryptography.fernet import Fernet

key = Fernet.generate_key()  # generate a key
file = open("encryption.key", "wb")
file.write(key)
file.close()
