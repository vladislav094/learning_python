class ListInstance:

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\t{attr} = {self.__dict__[attr]} \n'
        return result

    def __str__(self):
        return f"Instance of {self.__class__.__name__}," \
               f"{id(self)}," \
               f"{self.__attrnames()}"


class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'


x = Spam()
print(x)
