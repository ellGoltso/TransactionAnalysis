from functools import wraps

import json


def write_to_file(filename: str = None):
    """ Записывает результат функции в файл """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    result.to_json(filename, force_ascii = False, indent=4, orient='records', date_format='iso')
                else:
                    result.to_json('data/function_results.json', force_ascii = False, indent=4, orient='records', date_format='iso')
            except Exception as e:
                exc_str = f"{func.__name__} error: {e}."
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(exc_str, f)
                else:
                    with open('data/function_results.json', 'w', encoding='utf-8') as f:
                        json.dump(exc_str, f)

        return wrapper
    return decorator