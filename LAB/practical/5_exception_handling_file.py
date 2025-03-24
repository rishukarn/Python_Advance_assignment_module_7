

try:
    file=open('rishu.txt','r')
    f=file.read()
    print(f)
except FileNotFoundError:
    print('file not found ')
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was not opened, so no need to close it.")