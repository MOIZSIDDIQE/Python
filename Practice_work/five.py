count = 1

while count <=10:
    print("hello")
    print(count)
    count +=1    

# practice 1:
# No 1:
i =1
while i<=100:
    print(i)
    i +=1

# No:2
i =100
while i>=1:
    print(i)
    i -=1     

# No:3
n = int(input("Which number of table do you want. Enter your number :"))
i = 1
while i<=10:
    print(n*i)
    i +=1    

# No4:
lists=[] 

n = 10
i = 1
while i<=n:
    lists.append(i*i)
    i +=1

print(lists)

i=0
while i<len(lists):
    print(lists[i])
    i +=1

# No5:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 64,100)

num = 64
i =0
while i<len(tup):
    if(tup[i] == num):
        print(f"Found number on index {i}")
    i += 1

names = ["hassan","anus","muheeb","zafar"]
i= 0
name= "anus"
while i<len(names):
    if(names[i] == name):
        print(f"{name} is present in the class")
        break                                  #     To stop loop 
    elif(names[i] == "hassan"):
        print("hassan is suspended")
    i += 1



i =1
while i <= 10:
    if(i%2 != 0):
        i+=1
        continue                                  # To skip loop
    print(i)
    i +=1

numbers = [1,2,4,9,3,4,5,6,7,8,9,10]

for i in numbers:
    print(i)


name = "Hy everyone"

for i in name:
    print(i)

for c in name:
    if(c == "e"):
        print("Character found")
        break                                  # To stop loop
    print(c)
else:
    print("Character not found")

# P2 : No1

for i in tup:
    print(i)

find = 49

# P2 : No2

for i in tup:
    if(find == i):
        print(f"{find} is found in the tuple ")
        break                                  #     To stop loop