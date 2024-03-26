class Static:
    # # static property
    pro = [10]

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def method(self, age):
        self.age = age

    @staticmethod
    def s_method(self, age):
        print(age)


instance1 = Static("kdkkd")
instance2 = Static("kdkkd")
instance1.method(50)
instance1.s_method(120, 20)
print(instance2.age)
Static.s_method(20, 550)
