class One:
    def print_name(self, name) -> None:
        print(name)
        return 200


class two:
    def __init__(self, name) -> None:
        self.name = One()


k = two("faishal")
print(k.name.print_name("faishal"))
