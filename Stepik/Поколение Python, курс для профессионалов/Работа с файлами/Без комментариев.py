import sys

without_comm = [line for line in sys.stdin if line == '\n' or line.lstrip()[0]!='#']

print(*without_comm, sep='')