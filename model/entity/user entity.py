class User:
    def __init__(self, id, name, family, birthdate,username,pa):
        self.id = id
        self.name = name
        self.family = family
        self.birthdate = birthdate
        self.username = username
        self.pa = pa

    def to_tuple(self):
        return (self.id,self.name,self.family,self.birthdate,self.username,self.pa)