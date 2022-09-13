import random
from string import punctuation,ascii_letters,digits

sysmbols = punctuation + ascii_letters + digits
secured_random = random.SystemRandom() 
secure_password = "".join(secured_random.choice(sysmbols) for i in range(10))
print(secure_password)

