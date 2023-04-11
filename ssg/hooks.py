_callbacks = {}

def register(hook, order=0):
    def register_callback(func):
        setdefault(hook, {}).setdefault(order, []).append(func)
        return func
    return register_callback


