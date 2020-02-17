"""Homework 5 Task 3"""


class Observable:
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __str__(self):
        return (str(self.__class__.__name__) + ' '
                + str({i: getattr(self, i)
                       for i in dir(self) if not i.startswith('_')}))


class Isildur(Observable):
    pass


class Aragorn(Isildur):
    pass


King_1 = Isildur(King_of_Gondor=True, alive=False)
King_2 = Aragorn(foo=1, bar=5, _bazz=12, name="Amok", props=("One", "two"))

print("King_1:")
print(King_1)
print("King_2:")
print(King_2)
print()
print("King_2.foo =", King_2.foo)
print("King_2.name =", King_2.name)
print("King_2._bazz =", King_2._bazz)
