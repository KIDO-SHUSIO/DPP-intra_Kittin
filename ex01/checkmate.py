# โค้ดสี ANSI สำหรับแสดงผลใน Terminal
COLOR_RESET = "\033[0m"
COLOR_KING = "\033[1;33;41m"       # สีเหลือง ตัวหนา พื้นหลังแดง
COLOR_ATTACKER = "\033[1;31m"      # สีแดง ตัวหนา
COLOR_GRID = "\033[90m"          # สีเทาสำหรับเส้นและพิกัด

def checkmate(board, visualize=False):
    try:
        lines = board.strip().splitlines()
        if not lines:
            print("Error")
            return

        size = len(lines)
        king_pos = None
        king_count = 0

        for r in range(size):
            if len(lines[r]) != size:
                print("Error")
                return
            for c in range(size):
                if lines[r][c] == 'K':
                    king_count += 1
                    king_pos = (r, c)
        
        if king_count != 1:
            print("Error")
            return

        kr, kc = king_pos
        pieces = {'P', 'B', 'R', 'Q', 'K'}
        attacker_info = None

        # 1. เช็ค Rook (R) และ Queen (Q)
        rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in rook_dirs:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                char = lines[r][c]
                if char in pieces:
                    if char in ('R', 'Q'):
                        attacker_info = (char, r, c)
                    break
                r += dr
                c += dc
            if attacker_info:
                break

        if not attacker_info:
            bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in bishop_dirs:
                r, c = kr + dr, kc + dc
                while 0 <= r < size and 0 <= c < size:
                    char = lines[r][c]
                    if char in pieces:
                        if char in ('B', 'Q'):
                            attacker_info = (char, r, c)
                        break
                    r += dr
                    c += dc
                if attacker_info:
                    break

        # 3. เช็ค Pawn (P)
        if not attacker_info:
            pawn_positions = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
            for pr, pc in pawn_positions:
                if 0 <= pr < size and 0 <= pc < size:
                    if lines[pr][pc] == 'P':
                        attacker_info = ('P', pr, pc)
                        break

        # --- แสดงผลลัพธ์ ---
        if visualize:
            print(f"\n--- Board Analysis ({size}x{size}) ---")
            header = "    " + " ".join([f"{c}" for c in range(size)])
            print(f"{COLOR_GRID}{header}{COLOR_RESET}")
            print(f"{COLOR_GRID}   +" + "--" * size + f"+{COLOR_RESET}")

            for r in range(size):
                row_str = f"{COLOR_GRID}{r} |{COLOR_RESET} "
                for c in range(size):
                    char = lines[r][c]
                    if (r, c) == king_pos:
                        row_str += f"{COLOR_KING} K {COLOR_RESET}"
                    elif attacker_info and (r, c) == (attacker_info[1], attacker_info[2]):
                        row_str += f"{COLOR_ATTACKER} {char} {COLOR_RESET}"
                    else:
                        row_str += f" {char} "
                row_str += f"{COLOR_GRID}|{COLOR_RESET}"
                print(row_str)

            print(f"{COLOR_GRID}   +" + "--" * size + f"+{COLOR_RESET}")

            if attacker_info:
                piece_names = {'P': 'Pawn', 'B': 'Bishop', 'R': 'Rook', 'Q': 'Queen'}
                p_name = piece_names.get(attacker_info[0], attacker_info[0])
                print(f"Status: {COLOR_ATTACKER}CHECKED!{COLOR_RESET}")
                print(f"Attacked by: {p_name} ({attacker_info[0]}) at Row {attacker_info[1]}, Col {attacker_info[2]}")
            else:
                print(f"Status: SAFE (No Check)")
            print("---------------------------\n")

        if attacker_info:
            print("Success")
        else:
            print("Fail")

    except Exception:
        print("Error")