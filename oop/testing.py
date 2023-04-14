class Testing:
    count_arr = []
    total_age = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Testing.count_arr.append(name)
        Testing.total_age += age

    @staticmethod
    def print_arr_with_name():
        print(Testing.count_arr)

    @staticmethod
    def get_total_age():
        print(Testing.total_age)

    @classmethod
    def print_total_age(cls):
        print('1', cls.total_age)


class SubClass(Testing):
    ...


# a = Testing('Bob', 25)
# b = Testing("jack", 40)
# c = Testing('Ola', 22)
#
# Testing.print_arr_with_name()
# Testing.get_total_age()
#
# d = SubClass('Ivan', 10)
# d.print_total_age()


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        return self.func(*args)


@tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
