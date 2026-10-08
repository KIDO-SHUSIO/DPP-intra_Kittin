def checkmate(board):
    if not board or not isinstance(board, str):
        return

    lines = [line for line in board.strip('\n').split('\n') if line]
    if not lines:
        return

    size = len(lines)

    for line in lines:
        if len(line) != size:
            return

    king_pos = None
    king_count = 0
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        return

    kr, kc = king_pos

    pieces = {'P', 'B', 'R', 'Q', 'K'}

#--------------------------------------------------------------------------------

    pawn_attackers = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for pr, pc in pawn_attackers:
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

#--------------------------------------------------------------------------------

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            
            if piece in pieces:
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break  
                
            r += dr
            c += dc

#--------------------------------------------------------------------------------

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            
            if piece in pieces:
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break  
                
            r += dr
            c += dc

#-------------------------------------------------------------------------------- 

    print("Fail")