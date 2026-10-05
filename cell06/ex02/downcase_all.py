import sys

def downcase_it(string_val):
    return string_val.lower()

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        print(downcase_it(param))
else:
    print("none")

    # python cell06/ex02/downcase_all.py "HELLO WORLD" "I understood Arrays well!"