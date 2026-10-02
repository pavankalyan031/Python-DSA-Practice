# public
class Student:
    def __init__(self):
        self.name="Pavan"
        
s1=Student()
print(s1.name)


#protected
class Student:
    def __init__(self):
        self._name="Pavan"
        
s1= Student()
print(s1._name)


#private
class Student:
    def __init__(self):
        self.__name="Pavan"
        
s1=Student()
print(s1._Student__name)