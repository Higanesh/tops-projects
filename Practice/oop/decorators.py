
def dec(fx):
    def vfx(*args,**kwargs):
        print("calling before")
        fx(*args,**kwargs)
        print("calling after")
    return vfx

@dec

def test():
    print("test function calling....")

@dec
def add(a,b):
    print("add calling...")

@dec
def mycall():
    print("mycall calling...")

test()
mycall()
add(10,20)