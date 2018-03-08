def umpacking(*args): # tupla
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]

    print(arg1)
    print(arg2)
    print(others)


def umpacking2(**kwargs): #dicionario
    print(kwargs)


umpacking2(named = "teste", outro = "outros")

