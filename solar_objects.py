# coding: utf-8
# license: GPLv3


class Star:
    def __init__(self):

        self.space_type = "Star"


    def __repr__(self):
        self.m = 0
        """Масса звезды"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус звезды"""

        self.color = color_f("red")
        """Цвет звезды"""

        self.image = None
        """Изображение звезды"""


    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    type = "planet"
    """Признак объекта планеты"""

    def __init__(self):
        self.m = 0
        """Масса планеты"""
        self.x = 0
        """Координата по оси **x**"""
        self.y = 0
        """Координата по оси **y**"""
        self.Vx = 0
        """Скорость по оси **x**"""
        self.Vy = 0
        """Скорость по оси **y**"""
        self.Fx = 0
        """Сила по оси **x**"""
        self.Fy = 0
        """Сила по оси **y**"""
        self.R = 5
        """Радиус планеты"""
        self.color = color_f('red')
        """Цвет планеты"""
        self.image = None
        """Изображение планеты"""

        self.space_type = 'Planet'

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def from_hex(str):
    a1 = int(str[1:3:], 16)
    a2 = int(str[3:5:], 16)
    a3 = int(str[5::], 16)

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)
    ORANGE = (255, 100, 10)
    WHITE = (255, 255, 255)
    COLORS = {RED : "red", BLUE: "blue", YELLOW : "yellow", GREEN : "green",
              MAGENTA : "magenta", CYAN : "cyan", ORANGE : "orange", WHITE : "white"}
    return COLORS[(a1, a2, a3)]


def color_f(str):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)
    ORANGE = (255, 100, 10)
    WHITE = (255, 255, 255)
    COLORS = {"red": RED, "blue": BLUE, "yellow": YELLOW, "green": GREEN,
              "magenta": MAGENTA, "cyan": CYAN, "orange": ORANGE, "white": WHITE}
    return from_rgb(COLORS[str])
