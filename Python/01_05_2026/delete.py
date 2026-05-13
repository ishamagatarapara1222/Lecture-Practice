#Delete key-word
print("\nDelete key-word example:")

list_1 = [10,20,30,40]

print("Before deleting list_1:", list_1)

del list_1[3]

print("After deleting index :", list_1)
 
del list_1[2]

print("After deleting index:", list_1)

#Delete dictionary key

dict_1 = {"a" : 1 , "b" : 2}

del dict_1["a"]

print("Dictionary after delete:", dict_1)

#Tuple do note modify and delete
'''
t_1 = (1,2,3,4)

del t_1[0]
'''
#small program

print("\nSmall program:")

students = ["Alice","Rocky","Kevin","Rowan","Alice","alice"]

print("Origianl list:" ,students)

unique_students = list(set(students))

student_data = {name:len(name) for name in unique_students}

print("Student Data:",student_data)

#Create List, Tuple, Set and Dict using user input

user_input = input("Enter elements seprated by space:")

user_list = user_input.split()

print("User list:",user_list)

user_tuple = tuple(user_list)

print("User tuple:",user_tuple)

user_set = set(user_tuple)

print("User set:",user_set)

user_dict = {i:value for i , value in enumerate(user_list)}

print("User set", user_dict)

dict_input = input("Enter key:value seprated by space:")

my_dict = {}

pairs = dict_input.split()

for item in pairs:
    key , value = item.split(":")
    my_dict[key] = value

print("Disctionary:",my_dict)


