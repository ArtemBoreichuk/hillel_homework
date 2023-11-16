class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float))
                and isinstance(self.b, (int, float))
                and isinstance(self.c, (int, float))):
            return "Потрібно вводити тільки числа!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "З негативними числами нічого не вийде!"
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            return "Ура, можна побудувати трикутник!"
        else:
            return "Жаль, але з цього трикутник не зробити."


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class ExtTriangle(TriangleChecker, Triangle):
    def __init__(self, a, b, c):
        TriangleChecker.__init__(self, a, b, c)
        Triangle.__init__(self, a, b, c)


triangle_1 = ExtTriangle(3, 4, 5)
print(triangle_1.is_triangle())  # "Ура, можна побудувати трикутник!"
triangle_2 = ExtTriangle(-1, 2, 3)
print(triangle_2.is_triangle())  # "З негативними числами нічого не вийде!"
triangle_3 = ExtTriangle("a", 2, 3)
print(triangle_3.is_triangle())  # "Потрібно вводити тільки числа!"
triangle_4 = ExtTriangle(1, 1, 3)
print(triangle_4.is_triangle())  # "Жаль, але з цього трикутник не зробити."
