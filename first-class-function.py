def func(another):
    def call_another():
        another()
    return call_another


def lastOne():
    print("lastone")


print(func(lastOne)())
