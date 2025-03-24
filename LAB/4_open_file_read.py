#  Write a Python program to read the contents of a file and print them on the console.
#  Write a Python program to write multiple strings into a file.



# reading file 
file=open('rishu.txt','r')
f=file.read()
print(f)
file.close

# writing multiple string 

file=open('rishu.txt','a')
file.write('my name is bikash')
file.close