list = [4,1,3,2]

list.insert(3,6)
print(list)

list.append(5)
print(list)

list.remove(2)
print(list)

list.pop(3)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)


#                                                     Tuple
tup = (43,2,5,6,1,13,2,2,2,9)
print(tup[1:5])
print(tup.index(6))
print(tup.count(2))

# Practice:
listMovie = [input("Enter your 1st favorite movie name: "),input("Enter your 2nd favorite movie name: "),input("Enter your 3rd favorite movie name: ")]
print("Your three favorite movies",listMovie)

# Practice:
list1 = ['r','a','c','e','c','a','r']
list2 = [1,3,6,3,2]

copy1 = list1.copy()
copy2 = list2.copy()

copy1.reverse()
copy2.reverse()

if(list1 == copy1):
    print("List1 is palindrome")
else:
    print("List1 is not palindrome")

if(list2 == copy2):
    print("List2 is palindrome")
else:
    print("List2 is not palindrome")


# Practice:
gradeTuple = ("A","B","D","A","B","A","C","D")
print(gradeTuple.count("A"))

# Practice:
gradeList = ["A","B","D","A","B","A","C","D"]
gradeList.sort()
print(gradeList)