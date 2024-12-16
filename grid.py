def display_grid(grid): #Affiche la grille de jeu.
    print("\n")
    for i in range(0, 9, 3):
        print(f" {grid[i]}  |  {grid[i + 1]}  |  {grid[i + 2]} ")
        if i < 6:
            print("----|-----|----")
    print("\n")


def update_grid(grid, position, mark): #Met à jour la grille à la position donnée avec le symbole du joueur.
    if 0 <= position < len(grid) and isinstance(grid[position], int):  # Vérifie que la case est jouable (contient un numéro)
        grid[position] = mark
   
