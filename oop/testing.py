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


a = Testing('Bob', 25)
b = Testing("jack", 40)
c = Testing('Ola', 22)

Testing.print_arr_with_name()
Testing.get_total_age()

d = SubClass('Ivan', 10)
d.print_total_age()
