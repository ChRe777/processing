from functools import reduce
import shutil


def id(x):
    return x


def file_to_str(file):
    with open(file) as f:
        return f.read()


def str_to_json(str):
    import json

    return json.loads(str)


def many_to_many(xs, f):
    ys = []
    for x in xs:
        y = f(x)
        ys.append(y)
    return ys


def many_to_one(xs, f):
    y = reduce(f, xs)
    return y


def one_to_many(x, f):
    xs = f(x)
    return xs


def combine(*fns):
    def foo(x):
        for f in fns:
            x = f(x)
        return x

    return foo


def str_concat(x, y):
    return x + y


def dict_merge(x1, x2):
    x1.update(x2)
    return x1


def copy_folder(src, *dests):
    xs = []
    for dest in dests:
        x = shutil.copytree(src, dest, dirs_exist_ok=True)
        xs.append(x)
    return xs


def zero_to_n(x):
    return list(range(0, x))


def process_steps(x, steps):
    for step in steps:
        x = step(x)
    return x


def list_dir(path, fn=None):
    import os

    xs = os.listdir(path)
    if fn != None:
        xs = filter(xs, fn)
    return xs
