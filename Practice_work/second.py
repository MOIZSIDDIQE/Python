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

