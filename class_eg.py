class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def lastName (self):
        return self.name.split()[-1]

    def grow (self, how_much):
        self.age = self.age + how_much



sat = Worker('sathya sri',40)
bat = Worker('kaka jojo',30 )

sat.lastName()
sat.name
bat.grow(2)
bat.age

bat.age

print (bat.age)