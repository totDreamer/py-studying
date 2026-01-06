from re import sub, MULTILINE
from sys import stdin

def rm_comments(string):
    return sub(r'[ \t]*"""[^"]*"""\n|^[ \t]*#[^\n]+\n|[ \t]*#[^\n]+', '', string, flags=MULTILINE)

code = stdin.read()
print(rm_comments(code))