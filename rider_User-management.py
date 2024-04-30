from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.__email = email
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid) -> None:
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider name:{self.name}, email:{self.__email}')
