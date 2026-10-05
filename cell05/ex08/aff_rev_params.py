import sys

if len(sys.argv) > 2:
    for param in reversed(sys.argv[1:]):
        print(param)
else:
    print("none")

    #  python cell05/ex08/aff_rev_params.py "Python" "piscine" "hello"