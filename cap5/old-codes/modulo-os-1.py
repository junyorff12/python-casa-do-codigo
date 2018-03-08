import os

def os_func (path):
    dirs = os.listdir( path )
    for i in dirs:
        print(i)

def dir_or_file():
    for a in os.listdir("."):
        if os.path.isdir(a):
            print("d %s" % a)
        elif os.path.isfile(a):
            print("- %s" % a)


def exists():
    if os.path.exists("z"):
        print("Dir Z existe")
    else:
        print("dir Z não existe")

path = "/opt/"
# os_func(path)
# dir_or_file()
exists()


