def func(another):
    print(another())

    def call_another():
        another()
    return call_another

# decorator


@func
def lastOne():
    print("lastone")
    return 500
