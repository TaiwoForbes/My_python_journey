if "__main__" == __name__:
    from  encryption import encryptAndDecrypt
message = "Make me secret"
shift = 4
crypt = encryptAndDecrypt(message,shift)
print(crypt)
print(encryptAndDecrypt.__doc__)