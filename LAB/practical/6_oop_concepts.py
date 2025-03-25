#  11) Write a Python program to create a class and access the properties
# of the class using an object. 12) Write a Python program to demonstrate the use of local and
# global variables in a class.

global_var='I am global variable'
class car:

    

    def __init__(self,brand,model,year,value):
        self.brand=brand
        self.model=model
        self.year=year
        self.local_var=value # This is a local instance variable

    def display_info(self):
        print(f'Brand name {self.brand}:Model:{self.model} year:{self.year}')


    def show_variables(self):
        local_var = "I am a local variable"
        print(local_var)  # Accessing the local variable
        print(self.local_var)  # Accessing the instance variable
        print(global_var)  # Accessing the global variable


obj=car('Tata','i20',2018,'I am an instance variable')
obj.display_info()
obj.show_variables()