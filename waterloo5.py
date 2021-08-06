h = int(input(""))
w = int(input(""))
num = int(input(""))
stroke = []
for i in range(h * w):
    stroke.append("black")
for i in range(num):
    numbers = input().split()
    changelist = []
    if numbers[0] == "R":
        before = w * (int(numbers[1]) - 1) 
        for k in range(w):
            change = (k + 1) + before
            changelist.append(change -1)

    if numbers[0] == "C":
        before = w
        for k in range(h):
            change = (k) * before + int(numbers[1])
            changelist.append(change-1)    

    for i in range (len(changelist)):
        x = changelist[i]
        if stroke[x] == "black":
            stroke[x] = "gold"
        else:
            stroke[x] = "black"  
count = 0
for i in range(len(stroke)):
    if stroke[i] == "gold":
        count += 1
    
print(count)
print(stroke)
        
        
        
        
