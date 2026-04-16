# Mutable objects & identity

listA = [10, 20, 30]
listB = [10, 20, 30]
listC = listA

print("=================ID CHECK==================")
print(f"id(listA):{id(listA)}")
print(f"id(listB):{id(listB)}")
print(f"id(listC):{id(listC)}")

print("\n----------IS OPERATOR------------\n")
print(f"listA is listB: {listA is listB}")
print(f"listA is listC: {listA is listC}")

#modify using refrence

print("=======BEFORE MODIFICATION==========")
print(f"listA: {listA}")
print(f"listC: {listC}")

listC.append(40)

print("\n----- AFTER listC.append(40) -----")
print(f"listA: {listA}")  # will change
print(f"listC: {listC}")  # same object


#type examples

print("\n======TYPE EXAMPLES========\n")
print(f"type(42):{type(42)}")
print(f"type(4.2):{type(4.2)}")
print(f"type({{1, 2, 3}}):{type({1, 2, 3})}")

value = 42
print(f"type(value).__name__:{type(value).__name__}")

#function with multiple types

def analyze_data(data):
    print("\nProcessing:", data)

    if isinstance(data,int):
        return f"Integer Square:{data**2}"

    elif isinstance(data,str):
        return f"Reversed string:{data[::-1]}"

    elif isinstance(data,list):
        print("\n Original List length:{len(data)}")
        data.append("NEW")
        return f"Modified List: {data}"

    else:
        return f"Unsupported type: {type(data).__name__}"


#function call

print("\n===FUNCTION OUTPUT===\n")
print(analyze_data(7))
print(analyze_data("python"))
print(analyze_data([1, 2, 3]))
print(analyze_data((1, 2)))

#important concept check

print("\n----- MUTABLE CHECK -----")

my_list = [5, 6]
result = analyze_data(my_list)

print("\nAfter function call:")
print(f"my_list: {my_list}")
print(f"result: {result}")

print("\nObservation:")
print("Original list changed because lists are mutable and passed by reference.")


      

    
