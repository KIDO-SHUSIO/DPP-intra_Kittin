import sys
import os
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        return

    visualize_mode = False
    args = sys.argv[1:]

    # ตรวจสอบ Flag สำหรับเปิดโหมด Visualization
    if "-v" in args or "--visualize" in args:
        visualize_mode = True
        args = [arg for arg in args if arg not in ("-v", "--visualize")]

    # ประมวลผลไฟล์ที่ถูกส่งเข้ามา
    for file_path in args:
        if not os.path.isfile(file_path):
            print("Error")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                board = f.read()
            checkmate(board, visualize=visualize_mode)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()


    
#  python ex01\main.py -v ex01\valid_board.chess