V = lambda s,t: s/t

print(V(80,2))


def to_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@to_upper
def hello_world():
    return"Hello world"

print(hello_world())