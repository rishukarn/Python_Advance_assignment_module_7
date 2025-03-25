
# Write Python programs to demonstrate different types of inheritance (single, multiple,
# multilevel, etc.).

# single inheritance

class car:

    def __init__(self,brand,model,year):

        self.brand=brand
        self.model=model
        self.year=year



class info(car):

    def Display_info(self):
        print(f'Brand name:{self.brand} model:{self.model} year:{self.year}')


obj=info('Tata','i50',2023)
obj.Display_info()
        