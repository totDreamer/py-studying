gen_dict = {'A': 'U',
            'C': 'G',
            'T': 'A',
            'G': 'C'}
dnk_rnk = [gen_dict[s] for s in input()]
print(''.join(dnk_rnk))