def build_query_string(params):
    result = sorted([f'{key}={value}' for key, value in params.items()])
    return '&'.join(result)

print(build_query_string({"per": 14, "page": 7, "color": "red"}))
print(build_query_string(input()))