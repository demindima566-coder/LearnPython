def make_bread(f):
    def wrapper():
        print("Bread")
        f()
        print("Bread")
    return wrapper

def make_butter(f):
    def wrapper():
        print("Butter")
        f()
    return wrapper

def make_salat(f):
    def wrapper():
        print("Salat")
        f()
    return wrapper

def make_tomato(f):
    def wrapper():
        print("Tomato")
        f()

    return wrapper

def make_meat(f):
    def wrapper():
        print("Meat")
        f()
    return wrapper

@make_bread
@make_salat
@make_tomato
@make_meat
@make_butter
def make_sandwich():
    pass


make_sandwich()
