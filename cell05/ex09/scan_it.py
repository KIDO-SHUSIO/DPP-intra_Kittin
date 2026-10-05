import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(re.escape(keyword), text)
    
    if matches:
        print(len(matches))
    else:
        print("none")
else:
    print("none")


    # python cell05/ex09/scan_it.py "the" "the quick brown fox jumps over the lazy dog"