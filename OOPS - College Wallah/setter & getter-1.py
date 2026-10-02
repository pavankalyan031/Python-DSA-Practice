# getter
"""class Student:
    def __init__(self, name):
        self.__name=name
        
        
    def get_name(self):
        return self.__name
    
    
s1=Student("Pavan")
print(s1.get_name())"""


# setter
class Student:
    def __init__(self, name):
        self.__name=name
        
    def get_name(self):
      return self.__name
  
    def set_name(self, name):
        if name:
            self.__name=name
            
    
s1=Student("Pavan")
s1.set_name("Ravi")
print(s1.get_name())