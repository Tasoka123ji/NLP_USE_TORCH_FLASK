class Person:
    def __init__(self,name:str, age:int, id:int) -> None:
        self.__name = name 
        self.__age  = age
        self._id = id

    def get_name(self):
        return self.__name

    def set_name(self,name):
            if  not name is None:
                 self.__name = name 
    name = property(get_name,set_name)

    @property
    def age(self):
         return self.__age
    
    @age.setter
    def age(self,age):
        if isinstance(age,int):
              self.__age = age
        else :
             raise ValueError("age will be intager ")

person1 = Person(name = "Karen", age= 22, id = 1)
person1.age = 'hellp'
print(person1.age)
