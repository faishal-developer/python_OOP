from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Traiangle(Shape):
    def __init__(self, name) -> None:
        super().__init__(name)

    def area(self, height, adjacent):
        return (height*adjacent)/2


t1 = Traiangle("traindle")
print(t1.area(10, 20))
