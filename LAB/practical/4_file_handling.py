# Write a Python program to create a file and print the string into the
# file. 5) Write a Python program to read a file and print the data on the console. 6) Write a
# Python program to check the current position of the file cursor using tell()

with open('megha.txt','a+') as f:
    # f.write('My name is megha\n ')
    file=f.read()
    print(file)
    print(f.tell())