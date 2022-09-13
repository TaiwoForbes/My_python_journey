'''message = input("Enter your message to encrypt: ")
key = int(input("By how many character to shift: "))

secret_message = ""
for char in message:
    if  char.isalpha():
        char_code = ord(char)
        char_code = char_code + key
        if char == char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        elif char.islower():
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        secret_message += chr(char_code)
    elif char != char.isalpha():
        secret_message += char
print("Encrypted: ", secret_message)

# To Decrypt
key = -key
org_message = ""
for char in secret_message:
    if  char.isalpha():
        char_code = ord(char)
        char_code = char_code + key
        if char == char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        elif char.islower():
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        org_message += chr(char_code)
    elif char != char.isalpha():
        org_message += char
print("Decrypted: ", org_message)'''


def encryptAndDecrypt(message,key):
    """This function encrypt and decrypt a string with a specified keys to be shifted
       Message: The string to be encrypted and decrypted
       Key: The amount of character to shifted
    """
    # Stored the message into secret_message
    secret_message = ""
    # iterate through the strings/Message
    for char in message:
        #check if the char is alphabet
        if  char.isalpha():
            # if it is alphabet, get the character code and stored it in a vaiable called char_code
            char_code = ord(char)
            # Increment the character code by the key
            # if the character is A --> 65 + 4(key) = 69 ---> E
            char_code = char_code + key
            # Check if the character is upper
            if char == char.isupper():
                # If upper, maintain the range between 65 - 90
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                # If lower, maintain the range between 97 - 122
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
                # Continue adding the character code into the secret_message variable
            secret_message += chr(char_code)
        elif char != char.isalpha():
            # if not alphabet, then leave it unchanged
            secret_message += char
    
    # To Decrypt
    # Reverse the key
    key = -key
    # Place holder for the conversion
    org_message = ""
    for char in secret_message:
        if  char.isalpha():
            char_code = ord(char)
            char_code = char_code + key
            if char == char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            org_message += chr(char_code)
        elif char != char.isalpha():
            org_message += char
    return "Encrypted:{}\nDecrypted:{}".format(secret_message,org_message)
    
    
'''if "__main__" == __name__:
    test = encrypt("taiwo", 4)
    print(test)'''