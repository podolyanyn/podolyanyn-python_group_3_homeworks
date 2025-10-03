from functools import wraps

class TypeDecorators:
    @staticmethod
    def _convert_type(converter, fallback=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return converter(func(*args, **kwargs))
                except Exception:
                    return fallback if fallback is not None else func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def to_int(func=None):
        if func is None:
            return TypeDecorators._convert_type(int)
        return TypeDecorators._convert_type(int)(func)

    @staticmethod
    def to_str(func=None):
        if func is None:
            return TypeDecorators._convert_type(str)
        return TypeDecorators._convert_type(str)(func)

    @staticmethod
    def to_bool(func=None):
        def bool_converter(val):
            if isinstance(val, str):
                val = val.strip().lower()
                if val in {'true', '1', 'yes', 'y', 'on'}:
                    return True
                if val in {'false', '0', 'no', 'n', 'off'}:
                    return False
            return bool(val)
        if func is None:
            return TypeDecorators._convert_type(bool_converter)
        return TypeDecorators._convert_type(bool_converter)(func)

    @staticmethod
    def до_числа(func=None):
        def number_converter(val):
            try:
                return int(val)
            except (ValueError, TypeError):
                return float(val)
        if func is None:
            return TypeDecorators._convert_type(number_converter)
        return TypeDecorators._convert_type(number_converter)(func)


@TypeDecorators.to_int
def нічого_не_робити(рядок: str):
    return рядок

@TypeDecorators.to_bool
def do_something(рядок: str):
    return рядок


assert нічого_не_робити('25') == 25
assert do_something('True') is True
assert do_something('false') is False
assert do_something('abc') is True  # bool('abc') == True
