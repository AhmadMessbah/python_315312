class Employee:
    def __init__(self, id, name, family, age):
        self.id = id
        self.name = name
        self.family = family
        self.age = age

    def to_tuple(self):
        return (self.id,self.name,self.family,self.age)