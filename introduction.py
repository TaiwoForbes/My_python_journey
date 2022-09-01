def input_(msg, err_message = None):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            if err_message is not None:
                print(err_message)

user = input_(1,"one")
print(user)
user_ = input_(1)
print(user_)
