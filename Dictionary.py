student = {"name":"Atmaja","age":22,"college":"VIT Bhopal"}
print(student)
#printing individual values
#print(student["name"])
#keys can be string or integers
print(student.get("name"))
#For key that doesnot exist
print(student.get("phone","Not Found"))
student.update({"name":"Rohan"})
print(student.get("name"))
#Pop(removes a pair)
pop = student.pop("name")
print(pop)
print(student)
#length
print(len(student))
#Getting only the keys
#print(student.keys())
for key, value in student.items():
    print(key, value)
#Getting only the values
#print(student.values())