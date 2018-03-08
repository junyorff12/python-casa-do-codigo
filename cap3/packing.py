def new_user(active=False, admin=False):
    print(active)
    print(admin)


config = {"active": False, "admin": True}

# a = new_user(config.get('active'), config.get('admin')) #metodo normal

b = new_user(**config) # metodo packing gerando um dict

print(b)