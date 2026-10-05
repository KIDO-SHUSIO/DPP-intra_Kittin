import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    count = text.count('z')
    if count > 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")

    # python cell05/ex12/string_are_arrays.py "Zaz visits the zoo with Zazie"