#odd left
# even right
# 0 past
sumlist = []
flist2 = []
while True:
    code = input("")
    if code == "99999":
        break
    flist = []
    for i in range(len(code)):
        flist.append(code[i])
    flist2.append(flist)
    sum = int(flist[0]) + int(flist[1])
    sumlist.append(sum)
    

for i in range(len(flist2)):   
    if sumlist[i] % 2 == 0 and sumlist[i] != 0:
        print("right", end = " ")
        before = "right"
    if sumlist[i] % 2 == 1:
        print("left", end = " ")
        before = "left"
    if sumlist[i] == 0:
        print(before, end = " ")
    
    print(flist2[i][2] + flist2[i][3] + flist2[i][4])
           