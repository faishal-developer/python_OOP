# over riding
class Parent:
    def func(self):
        print("parent implementation")

    def forceImplement(self):
        print("working")
        raise NotImplementedError


class Child(Parent):
    def __init__(self, age) -> None:
        super().__init__()
        self.age = age

    def func(self):
        print("child implementation")

    # over riding
    def forceImplement(self):
        print("now working")

    # over loading
    def __add__(self, other):
        return self.age+other.age


c1 = Child(20)
c2 = Child(10)

c1.func()
c1.forceImplement()
print(c1+c2)
