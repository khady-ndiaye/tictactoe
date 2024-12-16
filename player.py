from Bot import ia_kea

def ask_player_number(): #Demande le nombre de joueurs, leurs prénoms et la difficulté (si nécessaire).
    while True:
        try:
            player_number = int(input("Combien de joueurs (1 ou 2) ? "))
            if player_number == 1:
                print("Vous jouez contre l'IA KEA.")
                player1 = input("Entrez le prénom du joueur : ")
                player2 = "KEA"

                # Demander le niveau de difficulté
                while True:
                    try:
                        difficulty = int(input("Choisissez le niveau 1 (facile) ou 2 (difficile) : "))
                        if difficulty in [1, 2]:
                            return player_number, player1, player2, difficulty
                        else:
                            print("Veuillez choisir entre 1 et 2.")
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
            elif player_number == 2:
                player1 = input("Entrez le prénom du joueur 1 : ")
                player2 = input("Entrez le prénom du joueur 2 : ")
                return player_number, player1, player2, None  # Pas de difficulté pour 2 joueurs
            else:
                print("Erreur : Le nombre maximum de joueurs est 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def play(player, mark, grid, difficulty=None): #Gère le tour d'un joueur (humain ou IA).
    if player == "KEA":
        print(f"C'est au tour de KEA ({mark} ) :")
        return ia_kea(grid, mark, difficulty)
    else:
        print(f"C'est au tour de {player} ({mark} ) :")
        while True:
            try:
                position = int(input("Choisissez une case (0-8) : "))
                if 0 <= position <= 8 and isinstance(grid[position], int):
                    return position
                else:
                    print("Case déjà occupée. Réessayez.")
            except ValueError:
                print("Entrez un numéro valide entre 0 et 8.")
