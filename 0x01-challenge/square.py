#!/usr/bin/python3
"""Look my square, it’s perfect? No? Should I change something?"""


class square():
    """Look my square, it’s perfect? No? Should I change something?"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Look my square, it’s perfect? No? Should I change something?"""
        for key, value in kwargs.items():
            """Look my square, it’s perfect? No? Should I change something?"""
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def PermiterOfMySquare(self):
        """Look my square, it’s perfect? No? Should I change something?"""
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Look my square, it’s perfect? No? Should I change something?"""
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":

    """Look my square, it’s perfect? No? Should I change something?"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
