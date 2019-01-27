from contextlib import contextmanager


@contextmanager
def mymanager():
    print('enter')
    yield
    print('exit')


def main():
    with mymanager():
        print("hello, world")


if __name__ == '__main__':
    main()
