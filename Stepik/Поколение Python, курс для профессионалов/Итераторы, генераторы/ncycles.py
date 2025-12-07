from itertools import tee, chain

def ncycles(iterable, times):
  yield from chain.from_iterable(tee(iterable, times))