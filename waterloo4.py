library = input("")
lib2 = []
for i in range(len(library)):
    lib2.append(library[i])  

before = lib2[0]
count = 0
ls = True
for i in range(1, len(lib2)):
    new = lib2[i]
    if new == "M" and before == "S":
        for k in range(i, len(lib2)):
            if lib2[k] == "L" and k > i:
                #print("Y")
                #print(lib2[i-1], lib2[k])                
                lib2[i-1] = lib2[k]
                lib2[k] = before                
                count += 1
                ls = False
                break
        if ls == True:
            lib2[i-1] = lib2[i]
            lib2[i] = before
            count += 1
    if new == "L" and before == "S":
        lib2[i-1] = lib2[i]
        lib2[i] = before       
        count += 1
    if new == "M" and before == "L":
        lib2[i-1] = lib2[i]
        lib2[i] = before      
        count += 1
    before = lib2[i]
    ls = True
print(lib2)
print(count)
            
        