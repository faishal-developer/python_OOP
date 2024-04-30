class Singleton:
    __instance = None

    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is Singleton')

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


first = Singleton()
second = Singleton.get_instance()
print(first)
print(second)
