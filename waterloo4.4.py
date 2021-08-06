library = input("")
lib2 = []
for i in range(len(library)):
    lib2.append(library[i])  
    
#first get all L up front
count = 0
for i in range(len(lib2)):
    isl = False
    if lib2[i] == "L":
        current = lib2[i]
        for k in range(len(lib2)):
            if (lib2[k] == "M" or lib2[k] == "S") and i > k:
                topletter = k
                isl = True
                break
        if isl :
            a = lib2[topletter]
            lib2[topletter] = lib2[i]
            lib2[i] = a    
            count += 1

for i in range(len(lib2)):
    is_S = False
    if lib2[i] == "M":
        current = lib2[i]
        for k in range(len(lib2)):
            if (lib2[k] == "S") and i > k:
                firsts = k
                is_S = True
                break
        if is_S :
            a = lib2[firsts]
            lib2[firsts] = lib2[i]
            lib2[i] = a    
            count += 1
print(lib2)   
print(count)