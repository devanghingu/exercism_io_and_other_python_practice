def do_flatten(iterable):
    nested_list = iterable[:]

    while nested_list:
        sublist = nested_list.pop(0)

        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        elif sublist or sublist == 0:
            yield sublist


def flatten(iterable):
    return [i for i in do_flatten(iterable)]