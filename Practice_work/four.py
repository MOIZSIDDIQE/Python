
student={
    "name":"Moiz",
    "Id":456,
    "age":18,
    "skills":["HTML","CSS","TYPESCRIPT","TAILWINDCSS","NODE.JS","PYTHON"],
    "Subjects":{
        "Class9th":{
            "math":89,
            "english":92,
            "total":472
        },
        "class10th":{
            "math":84,
            "english":86,
            "total":1152}
    }
}

print(student["skills"])

print(student["Subjects"]["class10th"])

print(student.keys())

print(student.values())

print(student.items())

print(student.get("skills"))

student.update({"FName":"Siddiq"})
print(student)

num = {1,2,4,9,3,4,5,6,7,8,9,10,"java"}

num.add("python")
print(num)

num.remove(3)
print(num)

print(num.pop())
print(num)


set2 = {"python" , "c",4,6,11,"typescript"}

print(num.union(set2)) # It will Conbine both sets.
print(num.intersection(set2))#It will return common value.


# Practice 1:
p1 ={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(p1)

# Practice 2:
p2 = {"python","java","C++","python","javascript","java","python","C++","C"}
print(len(p2))

# Practice 3:

marks= {}
p3 = int(input("Enter your English marks :"))
marks.update({"English" : p3 })

p3 = int(input("Enter your Math marks :"))
marks.update({"Math" : p3 })

p3 = int(input("Enter your Physics marks :"))
marks.update({"Physics" : p3 })

print(marks)