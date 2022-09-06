with open("fred.txt", 'w') as output:
    message = 'I"m alive '
    print(message)
    print(message, file = output)