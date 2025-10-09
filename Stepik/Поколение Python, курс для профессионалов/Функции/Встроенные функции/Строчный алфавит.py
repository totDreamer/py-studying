def all_lower_char(start=97):
    print(chr(start))
    if start == 122:
        return
    all_lower_char(start+1)
    
all_lower_char()