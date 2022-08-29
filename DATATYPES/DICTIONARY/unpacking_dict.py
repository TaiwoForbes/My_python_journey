def parrot(voltage, state, action):    
    print("This parrot wouldn't", action, end=' ')     
    print("if you put", voltage, "volts through it.", end=' ')    

    print("E's", state, "!") 

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"} 
parrot(**d)
print(d)
