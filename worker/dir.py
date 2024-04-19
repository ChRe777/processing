def copy_dir(src, *dests):
    import shutil

    xs = []
    for dest in dests:
        x = shutil.copytree(src, dest, dirs_exist_ok=True)
        xs.append(x)
    return xs


def list_dir(path, fn=None):
    import os

    xs = os.listdir(path)
    if fn != None:
        xs = filter(xs, fn)
    return xs
