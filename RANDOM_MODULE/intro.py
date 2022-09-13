# Create a random user password
import random
from string import punctuation,ascii_letters,digits

sysmbols = punctuation + ascii_letters + digits
secured_random = random.SystemRandom() 
secure_password = "".join(secured_random.choice(sysmbols) for i in range(10))
print(secure_password)
print()
print()


# Create a password with one punctation mark, one letter and three digits
alphabet = ascii_letters + digits
while True:
    password = "".join(random.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
    and any(c.isupper() for c in password)
    and sum(c.isdigit() for c in password) >= 3):
        break
print(password)
print()

# Creating a cryptography secured random number
from random import SystemRandom
secured = SystemRandom()

print([secured.randrange(10) for i in range(10)])
print()

# Random.shuffle() --> You can use random.shuffle() to mix up/randomize the items in a mutable and indexable sequence.
laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs)
print(laughs)
print()

# Random.choice() --> Takes a random element from an arbitrary sequence:
laughs = ["Hi", "Ho", "He"]
print(random.choice(laughs))
print()

# Random.sample() --> Like choice it takes random elements from an arbitrary sequence but you can specify how many:
print(random.sample(laughs,2))
print()
# Random.randrange() --> It works like range function but the last value is not inclusive
print(random.randrange(2,10))
# Random.randint() --> This return a random value between x and  y. The last value is included
print(random.randint(2,7))


# Random.random( --> Returns a random floating point number between 0 and 1:
random.random() # Out: 0.66486093215306317
# Randdom.uniform Returns a random floating point number between x and y (inclusive):
random.uniform(1, 8) # Out: 3.726062641730108