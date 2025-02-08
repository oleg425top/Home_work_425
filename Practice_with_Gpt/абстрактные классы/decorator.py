import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st =time.time()
        func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'время работы{dt} сек')
        return func(*args, **kwargs)
    return wrapper

def perimeter(func):
    def wrapper(*args):
        print(func(*args))
        s = sum(list(*args))
        return f'периметр равен {s}'

    return wrapper
@test_time
@perimeter
def figure(*args):
    res = ''
    if len(*args) == 1:
        res = 'это прямая'
    elif len(*args) == 3:
        res ='это треугольник'
    elif len(*args) == 4:
        if list(*args)[0] == list(*args)[1] == list(*args)[2] == list(*args)[3]:
            res = 'это квадрат'
        else:
            res = 'это прямоугольник'
    return res

triangle = (10, 10, 30)
print(figure(triangle))

square = (10, 10, 10 ,10)
print(figure(square))

