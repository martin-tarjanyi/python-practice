def create_list_with_comprehension():
    num_list = [i * 2 for i in range(10) if i % 2 == 0]
    for num in num_list:
        print(num)
    for num in num_list:
        print(num)


def create_generator():
    generator = (i * 2 for i in range(100) if i % 2 == 0)
    for num in generator:
        print(num)
    for num in generator:  # ineffective generator can be iterated over only once
        print(num)


def use_yield():
    for i in range(5):
        yield i * 3
    yield 42


if __name__ == '__main__':
    generator = use_yield()
    for i in range(6):
        print(generator.__next__())
