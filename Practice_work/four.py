
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

print(student["Subjests"]["class10th"])

print(student.keys())

print(student.values())

print(student.items())

print(student.get("skills"))