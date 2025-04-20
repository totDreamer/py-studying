import sys

reversed_in = [line.strip()[::-1] for line in sys.stdin]

print(*reversed_in, sep='\n')