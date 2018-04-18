def make_counter(count):
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

cont = make_counter(0)
cont()

cont()

cont()

