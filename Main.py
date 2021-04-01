class binary_Search(object):
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

r1 = binary_Search("James", "Green", 16)
r2 = binary_Search("Derek", "Blue", 23)

r1.introduce_self()
r2.introduce_self()

#r1 = binary_Search()
#r1.name = "Tom"
#r1.color = "red"
#r1.weight = 30

#r1.introduce_self()

#r2 = binary_Search()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 40

#r2.introduce_self()




