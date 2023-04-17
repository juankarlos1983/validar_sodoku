import itertools
s = '1'
for _ in range(8 - 1):
    s = "". join(str(len(list(group))) + key for key, group in itertools.groupby(s))

