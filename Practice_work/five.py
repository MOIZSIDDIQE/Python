# count = 1

# while count <=10:
#     print("hello")
#     print(count)
#     count +=1    

# # practice 1:
# # No 1:
# i =1
# while i<=100:
#     print(i)
#     i +=1

# # No:2
# i =100
# while i>=1:
#     print(i)
#     i -=1     

# # No:3
# n = int(input("Which number of table do you want. Enter your number :"))
# i = 1
# while i<=10:
#     print(n*i)
#     i +=1    

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
name= "anush"
while i<len(names):
    if(names[i] == name):
        print(f"{name} is present in the class")
        break                                  #     To stop loop 
    elif(names[i] != name):
        print("by")
    i += 1