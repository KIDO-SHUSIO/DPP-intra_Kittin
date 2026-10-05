import sys

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        if not param.endswith("ism"):
            print(f"{param}ism")
else:
    print("none")

    # python cell05/ex13/append_it.py "parallel" "egoism" "human"