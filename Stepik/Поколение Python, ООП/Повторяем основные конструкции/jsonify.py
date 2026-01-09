from functools import wraps
import json


def jsonify(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))

    return wrapper


@jsonify
def make_user(id, live, options):
    return {"id": id, "live": live, "options": options}


print(make_user(4, False, None))


@jsonify
def make_list(n):
    return list(range(1, n + 1))


print(make_list(10))
