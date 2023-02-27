routers = ["R1","R2","R3"]
ipadd = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

Dictionary = {'R1': "10.0.0.1", 'R2': "10.0.0.2", 'R3': "10.0.0.3"}
for a,b in Dictionary.items():
    print(a, ":", b)