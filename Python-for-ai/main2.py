# print("Hello world !")
# first_name = "Ritika"
# last_name = "Sharma"
# full_name = first_name + " " + last_name
# print(full_name)

# # Working with string methods 
# text = "Hello PYTHON"
# print(text.lower()) # converts the string to lowercase
# print(text.upper()) # converts the string to uppercase

# text = "python programming"
# print(text.capitalize()) # converts the first character to uppercase and the rest to lowercase

# # replace()
# # Syntax: string_name.replace(old, new)
# text = "I love python programming"
# new_text = text.replace("python","java")
# print(new_text)

# # Find peak element code 
# def peakElement(arr):
#     n = len(arr)
#     if(n==1):
#         return 0
#     if(arr[0] > arr[1]):
#         return 0;
#     if(arr[n-1] > arr[n-2]):
#        return n-1;
#     for i in range(n):
#               if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
#                 return i

# if __name__ == "__main__":
# 	arr = [1, 2, 4, 5, 7, 8, 3]
# 	print(peakElement(arr))

# File handling in python 
# with open("student.txt") as file:
#      data = file.read()


# print(data)

# with open("student.txt", "w") as file:
#      file.write("Hello world!")        //write erases the content

# with open("student.txt", "a") as file:
#      file.write("\nSimran")

# with open("student.txt", "r") as file:
#     print(file.readlines())

with open("student.txt", "r") as file:
    students = [line.strip() for line in file]  # "\n" ye hata deta hai

print(students)   


