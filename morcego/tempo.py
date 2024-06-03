import time as tm



def mtempo(espesifico=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if espesifico:
                i = tm.time()
                func(*args, **kwargs)
                f = tm.time()
                print(f - i)
            else:
                i = int(tm.time())
                func(*args, **kwargs)
                f = int(tm.time())
                total = f - i
                print(total, "s")
        return wrapper
    return decorator





























