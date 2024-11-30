
class A:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name,self.email)


class A1:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name,self.email)

class B(A,A1):
    
    def __init__(self, name, email):
        A.__init__(self,name,email)
        A1.__init__(self,name,email)
        # super().__init__(name,email)

a = A("Paras","paras@gmail.com")
b = B("Ganesh","ganesh@gmail.com")

b.show()

        