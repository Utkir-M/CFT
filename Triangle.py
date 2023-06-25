#код для вычисления прямого угла трегольника
def right_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return (a * a + b * b + c * c) - max(a, b, c) ** 2 == max(a, b, c) ** 2
    return False
#Тест
if __name__ == '__main__':
    a=3
    b=4
    c=5
    print(right_triangle(a, b, c))