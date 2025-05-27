# Base class
class A:
    def show(self):
        print("Show from A")

# First derived class
class B(A):
    def show(self):
        print("Show from B")

# Second derived class
class C(A):
    def show(self):
        print("Show from C")

# Class with multiple inheritance
class D(B, C):
    pass

# Create object of class D and call show()
d = D()
d.show()

# Print the MRO
print(D.__mro__)
