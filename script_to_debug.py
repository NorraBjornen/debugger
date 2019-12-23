import tracer

tracer.set_trace()


def foo(a, b):
    a = 10
    b = 14
    c = 3
    return a + b


if __name__ == '__main__':
    print(foo(1, 2))
