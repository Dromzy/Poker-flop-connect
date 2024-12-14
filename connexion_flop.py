import os
import sys
import pprint
import math
import unittest
from utils import *

# Constants of importance of draws.
# It will multiply the number of each draws with this number to better reflect
# the impact of the draw on the equity of the range.
# Thinking process is for exemple that you won't extract as much value when you
# hit a one card oesd than a regular oesd.
PONDERATION = {"straight": 10, "oesd": 5, "one_card_oesd": 3, "paired_oesd": 3, "gs": 2, "one_card_gs": 1, "paired_gs": 1, "double_gs": 10}


def main(range_file="range-test.txt", flop_file="flops-test.txt"):
    # Import range file. Must be in PIO format.
    with open(range_file, "r") as fichier_range:
        range = fichier_range.read()

    # Import flop file. Must be in PIO format with weights.
    with open(flop_file, "r") as fichier_flop:
        flops_file = fichier_flop.read()

    # Decomposition of range as combo + freq of the combo in the range.
    range_combos = decompose_range(range)

    # Decomposition of flop cards without suit.
    flop_decompose = flops_file.split(sep="\n")
    flop_decompose = [flops[0] + flops[2] + flops[4] for flops in flop_decompose]
    liste_flops = set(flop_decompose)

    # Verification of flop decomposition
    # print(liste_flops)

    range_combos_expanded = expand_combos_range(range_combos)

    # Verification of range frequencies
    # print(range_combos_expanded)

    # Decomposition of combos as absolute freq.
    combos_freq = dict(x.split(":") for x in range_combos_expanded)
    for cle, valeur in combos_freq.items():
        combos_freq[cle] = float(valeur)

    # Verification of combos decomposition
    # print(combos_freq)

    combos_pondere = ponderation_combo(combos_freq)

    # Final result of connections of the range on a given flop.
    def analyse_hands(combos_pondere, flop, ponderation):
        connexion = dict()
        compte_final2 = dict()
        compte_final = {"straight": 0, "oesd": 0, "one_card_oesd": 0, "paired_oesd": 0, "gs": 0, "one_card_gs": 0, "paired_gs": 0, "double_gs": 0}
        score_final = {"straight": 0.0, "oesd": 0.0, "one_card_oesd": 0.0, "paired_oesd": 0.0, "gs": 0.0, "one_card_gs": 0.0, "paired_gs": 0.0, "double_gs": 0.0}
        for combo_type, nombre_de_combo in combos_pondere.items():
            hand = convert_hand(combo_type[0], combo_type[1])
            board = generate_board(flop, hand)
            connexion = count_draw(flop, hand, board)
            # print("hand: ", hand, "\n" "board :", board, "\n", "result", connexion)  # Verification of connectivity of combos.
            for key, values in connexion.items():
                compte_final2[key] = values * nombre_de_combo
            # print("compte final 2", compte_final2)
            compte_final = {k: v + compte_final[k] for k, v in compte_final2.items()}
            # print("compte final", compte_final)
        score_final = {k: math.ceil(v * ponderation[k]) for k, v in compte_final.items()}
        # print("score final", score_final)
        return score_final

    # Fonction analyse des flops
    score_flop = dict()
    for flops in liste_flops:
        flop = convert_flop(flops)
        score_flop[flops] = analyse_hands(combos_pondere, flop, PONDERATION)

    # pprint.pprint(score_flop, width=1)

    # Calculate the final connexion score of a flop based on number of connexion and
    # Ponderation with the constants
    score_flop_final = float()
    score_flop_values = dict()
    for k, values in score_flop.items():
        for nombre_de_connexions in values.values():
            score_flop_final += nombre_de_connexions
        score_flop_values[k] = score_flop_final
        score_flop_final = 0

    # pprint.pprint(score_flop_values, width=1)

    # Sort all flop results
    resultat_tri = sorted(score_flop_values.items(), key=lambda t: t[1])  
    pprint.pprint(resultat_tri, width=1)
    return resultat_tri

if __name__ == "__main__":
    range_file = sys.argv[1] if len(sys.argv) > 1 else "range-test.txt"
    flop_file = sys.argv[2] if len(sys.argv) > 2 else "flops-test.txt"
    main(range_file, flop_file)

