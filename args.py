# *args **kwargs

# *args allows function to accept as many postional arguments as you want.
def super_func(*args):
    return sum(args)

# *kwargs

super_func(1, 2, 3, 4, 5)
