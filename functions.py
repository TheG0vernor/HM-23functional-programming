from constants import LOG_DIR


def das_mapping(col, data=None):
    """Принимает номер колонки (может принять массив) и возвращает требуемую колонку из массива"""
    if data is None:
        data = das_data()
    col = int(col)
    result = map(lambda v: v.split(' ')[col], data)
    return list(result)


def das_filter(str_, data=None):
    """Принимает значение (может принять массив) и возвращает строки с этим значением"""
    if data is None:
        data = das_data()
    result = filter(lambda v: v if str_ in v else None, data)
    return list(result)


def unique_(data):
    """Вернет массив с уникальными значениями"""
    return list(set(data))


def sorted_(asc, data=None):
    """Сортирует массив"""
    if data is None:
        data = das_data()
    if asc == 'asc':
        return sorted(data)
    elif asc == 'desc':
        return sorted(data, reverse=True)


def limit(value, data=None):
    """Лимитирует вывод данных с массива"""
    if data is None:
        data = das_data()
    value = int(value)
    counter = 0
    result = []
    while counter < value:
        for i in data:
            result.append(i)
            counter += 1
            if counter == value:
                break

    return result


def das_data():
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v.strip(), f)
        return list(data)
        # data = f.read()
        # data = data.strip()
        # data = data.split('\n')
        # return data
