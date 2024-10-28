def parrot(hello=None, default="Squawk!"):
    if hello is None:
        print(default)
        return default
    else:
        print(hello)
        return hello


    
