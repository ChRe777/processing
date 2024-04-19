def combine(*fns):
    def foo(x):
        for f in fns:
            x = f(x)
        return x

    return foo
