message = input("Enter a string: ").strip(" ")
secret_message = ""
for char in message:
    secret_message = secret_message + str(ord(char) - 23 )
print("Secret Message: ", secret_message)
message = ""
for i in range(0, len(secret_message)- 1,2):
    char_code = secret_message[i] + secret_message[i + 1]
    message = message + chr(int(char_code) + 23 )
print("Original Message: ", message)