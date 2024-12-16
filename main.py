from grid import display_grid, update_grid
from player import ask_player_number, play
from victory_check import player_wins
import sys

def main():
    print("Bienvenue au Tic Tac Toe! 🎮")

    while True:  # Demander le nombre de joueurs, leurs noms et la difficulté
        player_number, player1, player2, difficulty = ask_player_number()

        # Initialiser la grille avec les numéros de 0 à 8
        grid = list(range(9))
        display_grid(grid)

        # Initialiser le tour de jeu
        round = 0
        while any(isinstance(x, int) for x in grid):  # Continue tant qu'il reste des cases avec numéro
            # Déterminer le joueur actuel et son symbole
            actual_player = player1 if round % 2 == 0 else player2
            mark = "☀️" if round % 2 == 0 else "❤️"

            # Obtenir la position choisie
            position = play(actual_player, mark, grid, difficulty)

            # Mettre à jour la grille
            update_grid(grid, position, mark)
            display_grid(grid)

            # Vérifier si le joueur a gagné
            if player_wins(grid, mark):
                if actual_player == "KEA":  # Si KEA gagne contre un joueur
                    print(f"Oh non ! Vous avez perdu contre KEA ! 😜🤖")
                else:  # Victoire d'un joueur
                    print(f"Félicitations, {actual_player} a gagné ! 🥳🎉")
                break
            round += 1
        else:
            print("Match nul ! Aucun gagnant. 😩")

        # Demander si les joueurs veulent rejouer
        while True: # Boucle principale pour rejouer ou arrêter
            replay = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()
            if replay in ["oui", "o"]:
                print("Relançons une nouvelle partie ! 🤓")
                break
            elif replay in ["non", "n", "no"]:
                print("Merci d'avoir joué ! À bientôt. 👋")
                sys.exit()
            else:
                print("Choisissez entre oui et non. 😜")

main()
