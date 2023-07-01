def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    def resolver(board: list[list[int]]) -> bool:
        l, c = casa_vazia(board)
        if l == None or c == None:
            return True 
        for numero in range(1, 10):
            board[l][c] = numero
            if is_valid(board) and resolver(board): 
                return True
            board[l][c] = 0 
        return False
    if resolver(board):
        return board
    else:
        raise ValueError

def is_valid(board: list[list[int]]) -> bool:
    for l in range(9):
        for c in range(9):
            numero = board[l][c]
            if numero != 0:
                for coluna in range(9):
                    if coluna != c and board[l][coluna] == numero:
                        return False
                for linha in range(9):
                    if linha != l and board[linha][c] == numero:
                        return False
                inicio_linha = 3 * (l // 3) 
                inicio_coluna = 3 * (c // 3)
                for linha in range(inicio_linha, inicio_linha + 3):
                    for coluna in range(inicio_coluna, inicio_coluna + 3):
                        if (linha != l or coluna != c) and board[linha][coluna] == numero:
                            return False
    return True

def casa_vazia(board: list[list[int]]) -> tuple[int, int]:
    for l in range(9):
        for c in range(9):
            if board[l][c] == 0:
                return l, c
    return None, None