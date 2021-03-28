#decorator

def header(some_func):
    def inner(*args, **kwargs):
        print("<h1>")
        some_func(*args, **kwargs)
        print("</h1>")
    return inner


def table(some_func):
    def inner(*args, **kwargs):
        print("<table>")
        some_func(*args, **kwargs)
        print("</table>")
    return inner


@header # say = header(say)
@table
def say(name, surename, age):
    print("hello", name, surename, age)


say("Yarek", "Lytvyniuk", 34)
