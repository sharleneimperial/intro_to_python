my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo"]

num_students = len(my_class)
print("There are", num_students, "students in the class")

my_class.append("Sonyl")
print(my_class)
print(my_class[2])
print(my_class.pop(0))

my_class.insert(1,my_class.pop())
print(my_class)

