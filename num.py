data = input("enter data")
dat = data.split(" ")
a = 0
b = 0
no = 0
t = 0
clas = int(input("Enter no of classes"))
for i in range(len(dat)):
    dat[i] = float(dat[i])
    a = a+1
r1 = float(input("Enter Staring Range"))
r2 = float(input("Enter ending Range"))
while no <= clas:
    b = 0
    for i in dat:
        if i >= r1 and i <=r2:
            b =b +1
            t =t +1
    print(b)
    r1 = r2
    r2 = float(input("Enter ending Range"))
    no = no+1
    
print(a)
print(f"total frequency{t}")



