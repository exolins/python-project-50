
from collections import namedtuple
from itertools import chain

Option = namedtuple("Option", ("old_value", "new_value"))
Diff = namedtuple('Diff', ('has_first', 'has_second', 'first_dict', 'second_dict', 'status', 'first_value', 'second_value', 'has_childrens', 'childrens'))
def diff(first, second):
    result =[]

    keys = first.keys() | second.keys()
    for key in keys:
        first_flag = key in first
        second_flag = key in second
        name = key
        if first_flag: 
            first_dict = isinstance(first[key], dict)
        if second_flag:
            second_dict = isinstance(second[key], dict)
        if first_dict and second_dict:
            result = diff(first[key], second[key])
        if not first_flag:
            result.append(Diff(
                              'has_first' = first_flag
                              'has_second' = second_flag
                              '
                          ))
        if not second_flag:
            result = ('del', first[key])
        match first_flag, second_flag, first_dict, second_dict:
            case True, True, False, False:
                if first[key] == second[key]:
                    result = ('same', first[key])
                else:
                    result = ('update', first[key], second[key])
            case True, True, True, False:
                result = ('update', first[key], second[key])


