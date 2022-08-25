import datetime
today = datetime.datetime.now()
tomorrow  = today + datetime.timedelta(days=1)
print(tomorrow)
yesterday = today - datetime.timedelta(days=1)
print("Yesterday:{}".format(yesterday) )