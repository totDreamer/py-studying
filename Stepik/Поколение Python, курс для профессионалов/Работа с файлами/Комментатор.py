import sys

comm_count = len([line.strip() for line in sys.stdin if line.strip()[0]=='#'])

print(comm_count)