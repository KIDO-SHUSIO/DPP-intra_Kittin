import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + 'Z' * (8 - len(s)))

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
else:
    print("none")

    # python cell06/ex04/methods_everywhere.py 'lol' 'physically' 'backpack'