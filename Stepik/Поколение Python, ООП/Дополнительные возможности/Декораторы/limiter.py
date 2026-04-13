def limiter(limit, unique, lookup):
    def decorator(cls):
        instances = {}
        order = []

        def wrapper(*args, **kwargs):
            if unique in kwargs:
                obj_id = kwargs[unique]
            else:
                pos = list(cls.__init__.__code__.co_varnames[1:]).index(unique)
                obj_id = args[pos] if pos < len(args) else None

            if obj_id in instances:
                return instances[obj_id]

            if len(instances) >= limit:
                return order[0] if lookup == "FIRST" else order[-1]

            new_instance = cls(*args, **kwargs)
            instances[obj_id] = new_instance
            order.append(new_instance)
            return new_instance

        return wrapper

    return decorator
