import sys, pickle

with open(input(), 'rb') as f:
    fun = pickle.load(f)
    args = list(map(str.strip, sys.stdin))
    print(fun(*args))