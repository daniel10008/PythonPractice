class A:
    def y (self):
        print("Y inside A class")
class B(A):
    pass
class C(A):
   pass
class D(C,B):
    pass
d =D()
d.y()