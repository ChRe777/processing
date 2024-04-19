import os


def list_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    xs = os.listdir(dir_path)
    return xs


def remove_file_ext(file_name):
    file_name, _ = os.path.splitext(file_name)
    return file_name


def names(xs):
    #
    # Remove __init__.py, __pychache__
    #
    xs = filter(lambda x: x.startswith("__") == False, xs)
    #
    # Remove file extension
    #
    xs = map(lambda x: remove_file_ext(x), xs)
    return list(xs)


def get_all():
    return names(list_dir())


__all__ = get_all()
