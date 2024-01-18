import random

def ia(board, signe):
    empty_cells = [i for i, cell in enumerate(board) if cell == 0]

    for cell in empty_cells:
        # Vérifiez si l'IA peut gagner en jouant à cette position
        if is_winning_move(board, cell, signe):
            return cell

    for cell in empty_cells:
        # Vérifiez si le joueur peut gagner en jouant à cette position et bloquez-le
        opponent_signe = 'O' if signe == 'X' else 'X'
        if is_winning_move(board, cell, opponent_signe):
            return cell

    # Si aucune opportunité de gagner n'est détectée, choisissez une position aléatoire
    if empty_cells:
        return random.choice(empty_cells)

    return False

def is_winning_move(board, move, signe):
    # Créez une copie temporaire du tableau pour vérifier les mouvements possibles
    temp_board = board.copy()
    temp_board[move] = signe

    # Vérifiez les lignes horizontales, verticales et diagonales pour déterminer une victoire
    for i in range(3):
        if (temp_board[i * 3] == temp_board[i * 3 + 1] == temp_board[i * 3 + 2] == signe or
            temp_board[i] == temp_board[i + 3] == temp_board[i + 6] == signe):
            return True

    if (temp_board[0] == temp_board[4] == temp_board[8] == signe or
        temp_board[2] == temp_board[4] == temp_board[6] == signe):
        return True

    return False