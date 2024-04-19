def file_to_str(file):
    with open(file) as f:
        return f.read()


def str_to_file(str, file):
    with open(file=file, mode="w") as f:
        return f.write(str)



