import sys

params = sys.argv[1:]

if len(params) > 0:
    print(f"parameters: {len(params)}")
    for param in params:
        print(f"{param}: {len(param)}")
else:
    print("none")

    # python cell05/ex11/count_it.py "Game" "of" "Thrones"