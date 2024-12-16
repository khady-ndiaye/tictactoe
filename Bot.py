import random

def ia_kea(grid, mark, difficulty): #IA KEA : joue soit aléatoirement (facile) soit de manière stratégique (difficile).

 #Permet à KEA d'identifier son adversaire
    if mark == "☀️" :
        opponent = "❤️"
    else :
        opponent = "☀️"
        
    winning_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]

    # Mode facile : jouer dans une case vide aléatoire
    if difficulty == 1:
        empty_positions = [i for i in grid if isinstance(i, int)]
        return random.choice(empty_positions)

    # Mode difficile : jouer pour gagner, bloquer ou jouer stratégiquement
    if difficulty == 2:
        # Étape 1 : Jouer au centre si disponible
        if isinstance(grid[4], int):
            return 4

        # Étape 2 : Vérifier les combinaisons pour bloquer ou gagner
        for combination in winning_combination:
            boxes = [grid[i] for i in combination]
            # Bloquer l'adversaire
            if boxes.count(opponent) == 2 and any(isinstance(grid[i], int) for i in combination):
                return next(i for i in combination if isinstance(grid[i], int))
            # Jouer pour gagner
            if boxes.count(mark) == 2 and any(isinstance(grid[i], int) for i in combination):
                return next(i for i in combination if isinstance(grid[i], int))

        # Étape 3 : Jouer dans un coin si disponible
        for i in [0, 2, 6, 8]:  # Coins
            if isinstance(grid[i], int):
                return i

        # Étape 4 : Jouer dans une case vide restante
        return next(i for i in range(9) if isinstance(grid[i], int))
