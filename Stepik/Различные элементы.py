def unique(*, list : list):
    count = 0
    use_elements = []
    for element in list:
        if element not in use_elements:
            use_elements.append(element)
            count += 1
    return count

print(unique(list=input().split()))