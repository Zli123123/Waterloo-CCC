number = int(input(""))
listofstuff = []
list2 = []
for i in range(number):
    name = input("")
    listofstuff.append(name)
    bid = int(input(""))
    list2.append(bid)
highestbid = max(list2)
for i in range(number):
    if highestbid == list2[i]:
        print(listofstuff[i])
        break
    