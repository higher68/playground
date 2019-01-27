class Manager(object):
    def __enter__(self):
        """最初に実行される(前処理)
        """
        print('enter')

    def __exit__(self, exc_type, exc_value, traceback):
        """最後に実行される(後処理)
        """
        print('exit')


def main():
    with Manager():
        print("hello, world")


if __name__ == '__main__':
    main()
