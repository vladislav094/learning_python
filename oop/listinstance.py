# class ListInstance:
#
#     def __attrnames(self):
#         result = ''
#         for attr in sorted(self.__dict__):
#             result += f'\t{attr} = {self.__dict__[attr]} \n'
#         return result
#
#     def __str__(self):
#         return f"Instance of {self.__class__.__name__}," \
#                f"{id(self)}," \
#                f"{self.__attrnames()}"
#
#
# class Spam(ListInstance):
#     def __init__(self):
#         self.data1 = 'food'
#
#
# x = Spam()
# print(x)


class People:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def get_old(self):
        return self.__old

    @get_old.setter
    def get_old(self, old):
        self.__old = old

    # old = property(get_old, set_old)

a = People('Ivan', 25)
print(a.get_old)
a.get_old = 30
print(a.get_old)
