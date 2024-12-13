def check_5(count_of_classes):
    result_list = all([any(map(lambda x: x == '5', [input().split()[1] for _ in range(int(input()))])) for _ in
                       range(count_of_classes)])
    result = 'YES' if result_list else 'NO'
    return result


print(check_5(int(input())))
