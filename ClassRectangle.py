class Rectangle:

    def __init__(self,a=1,b=1):
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculate_P(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return f"Rectangle:A = {self.a}, b={self.b}"

    # def __repr__(self):
    #      return f"WOW"
    #
    #  def __str__(self):
    #     return f"fufufufufufufufu"

    def __del__(self):
        pass

# rect1 = Rectangle(10,15)
# rect2 = Rectangle(b=15,a=10)
# rect3 = Rectangle(20)
# rect4 = Rectangle()
#
# print(rect1.get_info())
# print(rect2.get_info())
# print(rect3.get_info())
# print(rect4.get_info())

# rect = Rectangle()
# print(rect)