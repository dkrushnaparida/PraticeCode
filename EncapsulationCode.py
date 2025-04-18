## bundling of attributes and methods inside a single class know as Encapsulation 

class Employee:
    def __init__(self,e_count):
        self.__e_count = e_count


    def get_data(self):
        return self.__e_count
    
e_data = Employee(1000)

print(e_data.get_data())

print(e_data.__e_count)