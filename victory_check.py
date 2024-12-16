def player_wins(grid, mark): #Vérifie si un joueur avec un symbole donné a gagné.
    winning_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for combination in winning_combination:
        if all(grid[i] == mark for i in combination):
            return True
    return False

