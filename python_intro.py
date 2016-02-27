SHORT_FUR = "krotkie"
LONG_FUR = "dlugie"

class Cat(object):
    def __init__(self, fur_length):
        self.fur_len = fur_length

    def meow(self, count):
        for i in range (count):
            print("meow", "my fur length is", self.fur_len)



kitty = Cat(SHORT_FUR)
print(kitty.fur_len)
kitty.meow(2)


kitty2 = Cat(LONG_FUR)
print(kitty2.fur_len)
kitty2.meow(4)
