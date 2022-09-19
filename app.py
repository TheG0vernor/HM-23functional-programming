from flask import Flask, abort, request

from constants import LOG_DIR
from functions import filter_and_mapping, das_filter, das_mapping, unique_, limit, mapping_and_filter, sorted_

app = Flask(__name__)


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')
        value2 = request.args.get('value2')
        file_name = request.args.get('file_name')
        if file_name not in LOG_DIR:
            abort(400)

        # блок кода, где cmd1 == filter
        elif cmd1 == 'filter' and cmd2 == 'map':
            return filter_and_mapping(str_=value1, col=value2)
        elif cmd1 == 'filter' and cmd2 == 'limit':
            data = das_filter(str_=value1)
            return limit(value=value2, data=data)
        elif cmd1 == 'filter' and cmd2 == 'unique':
            data = das_filter(str_=value1)
            return unique_(data=data)
        elif cmd1 == 'filter' and cmd2 == 'sort':
            data = das_filter(str_=value1)
            return sorted_(data=data, asc=value2)

        # блок кода, где cmd1 == map
        elif cmd1 == 'map' and cmd2 == 'unique':
            data = das_mapping(col=value1)
            return unique_(data=data)
        elif cmd1 == 'map' and cmd2 == 'limit':
            data = das_mapping(col=value1)
            return limit(value=value2, data=data)
        elif cmd1 == 'map' and cmd2 == 'filter':
            return mapping_and_filter(col=value1, str_=value2)
        elif cmd1 == 'map' and cmd2 == 'sort':
            data = das_mapping(col=value1)
            return sorted_(data=data, asc=value2)

        # блок кода, где cmd1 == sort
        elif cmd1 == 'sort' and cmd2 == 'limit':
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

        # блок кода, где cmd1 == limit
        elif cmd1 == 'limit' and cmd2 == 'map':
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
        else:
            abort(400)
    except:
        abort(400)
