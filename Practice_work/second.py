# endwith function : wo function hota ha jo value hum ()me pass kare ke last ka text  agar ya ho to true otherwise false.
# Example:
Name2 = "i am elder the elder brother"
print(Name2.endswith("er"))

#capatalize function : ya func str ke start ke letter ko capatale kar deta ha or dosre sab ko lowercase.
# Example:
Name3 = "i am elder the Elder Brother"
print(Name3.capitalize())
print(Name3.find("B")) 
print(Name3.count("e"))
print(Name3.replace("Elder","younger"))

age = int(input("Enter age: "))
if( age >= 18):
    if(age >=30):
        print("Can't Apply for Government job")
    else:
        print("Eligible for Government job")
else:
    print("Not Eligible for Government job")

#                                                       practice         
N_input = input("Enter Your Name: ")
print(len(N_input))

#                   practice         
buy = "I bought a Laptop for only $1000 dollar."
print(buy.count("f"))

grade= int(input("Enter Marks: "))

if(grade >= 90):
    print("Grade: A")
elif(grade >=80 and grade<90):
    print("Grade: B")
elif(grade >=70 and grade <80):
    print("Grade: C")
elif(grade >=50 and grade<70):
    print("Grade: D")
else:
    print("FAIL")

numInput = int(input("Enter Number: "))
if(numInput%2 == 0):
    print("Number is even")
else:
    print("Numner is odd")

array = ["Moiz",18,85.86,"Karachi"]
array[1["M"]] = "y"
print(array[0])

numberArray= [34,56,55,2,44,98,76,59,60,45,65]
print(numberArray[:6])
print(numberArray[4:])
print(numberArray[-5:-2])
print(numberArray[-8:])

