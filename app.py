from flask import Flask, abort, request

from constants import LOG_DIR
from services import limit_in_cmd1, sort_in_cmd1, map_in_cmd1, filter_in_cmd1

app = Flask(__name__)


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')
        value2 = request.args.get('value2')
        file_name = request.args.get('file_name')
        if file_name not in LOG_DIR:
            abort(400, 'несоответствие имени файла')
        elif cmd1 == 'filter':
            return filter_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'map':
            return map_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'sort':
            return sort_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'limit':
            return limit_in_cmd1(cmd1, cmd2, value1, value2)
        else:
            abort(400, 'введены недопустимые данные')
    except Exception as e:
        abort(400, e)
