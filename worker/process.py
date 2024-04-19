def process_steps(x, steps):
    for step in steps:
        x = step(x)
    return x


def many_to_many(xs, f):
    ys = []
    for x in xs:
        y = f(x)
        ys.append(y)
    return ys


def many_to_one(xs, f):
    from functools import reduce

    y = reduce(f, xs)
    return y


def one_to_many(x, f):
    xs = f(x)
    return xs
