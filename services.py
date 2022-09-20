from flask import abort

from functions import limit, das_filter, unique_, sorted_, das_mapping

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
В данном файле производится обработка post-запросов на сервер 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def filter_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'filter' and cmd2 == 'map':
            data = das_filter(str_=value1)
            return das_mapping(col=value2, data=data)
        elif cmd1 == 'filter' and cmd2 == 'limit':
            data = das_filter(str_=value1)
            return limit(value=value2, data=data)
        elif cmd1 == 'filter' and cmd2 == 'unique':
            data = das_filter(str_=value1)
            return unique_(data=data)
        elif cmd1 == 'filter' and cmd2 == 'sort':
            data = das_filter(str_=value1)
            return sorted_(data=data, asc=value2)
    except Exception as e:
        abort(400, e)


def map_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'map' and cmd2 == 'unique':
            data = das_mapping(col=value1)
            return unique_(data=data)
        elif cmd1 == 'map' and cmd2 == 'limit':
            data = das_mapping(col=value1)
            return limit(value=value2, data=data)
        elif cmd1 == 'map' and cmd2 == 'filter':
            data = das_mapping(col=value1)
            return das_filter(str_=value2, data=data)
        elif cmd1 == 'map' and cmd2 == 'sort':
            data = das_mapping(col=value1)
            return sorted_(data=data, asc=value2)
    except Exception as e:
        abort(400, e)


def sort_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'sort' and cmd2 == 'limit':
            data = sorted_(asc=value1)
            return limit(value=value2, data=data)
        elif cmd1 == 'sort' and cmd2 == 'filter':
            data = sorted_(asc=value1)
            return das_filter(str_=value2, data=data)
        elif cmd1 == 'sort' and cmd2 == 'unique':
            data = sorted_(asc=value1)
            return unique_(data=data)
        elif cmd1 == 'sort' and cmd2 == 'map':
            data = sorted_(asc=value1)
            return das_mapping(col=value2, data=data)
    except Exception as e:
        abort(400, e)


def limit_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'limit' and cmd2 == 'map':
            data = limit(value=value1)
            return das_mapping(col=value2, data=data)
        elif cmd1 == 'limit' and cmd2 == 'filter':
            data = limit(value=value1)
            return das_filter(str_=value2, data=data)
        elif cmd1 == 'limit' and cmd2 == 'sort':
            data = limit(value=value1)
            return sorted_(data=data, asc=value2)
        elif cmd1 == 'limit' and cmd2 == 'unique':
            data = limit(value=value1)
            return unique_(data=data)
    except Exception as e:
        abort(400, e)
