
class Pen:

    def __init__(self,id,name):
        self.name = name
        self.id = id

    def show(self):
        print("show something: ")
        print(self.id,self.name)

p1 = Pen(10,"Paras")
p1.show()

p2 = Pen(20,"Ganesh")
p2.show()

p3 = Pen(30,"Sagar")
p3.show()