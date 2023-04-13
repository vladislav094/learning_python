class Block:
    # Good Luck!
    def __init__(self, arr):
        self.arr = list(arr)

    def get_width(self):
        return self.arr[0]

    def get_length(self):
        return self.arr[1]

    def get_height(self):
        return self.arr[2]

    def get_volume(self):
        return self.arr[0] * self.arr[1] * self.arr[2]

    def get_surface_area(self):
        return 2 * (self.arr[1] * self.arr[0] + self.arr[1] * self.arr[2] + self.arr[0] * self.arr[2])


b = Block([2, 4, 6])
print(b)

print(b.get_width())
print(b.get_length())
print(b.get_height())
print(b.get_volume())
print(b.get_surface_area())
