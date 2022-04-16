import os
import pprint
import math


# Import range file.  Must be in PIO format.
with open("range.txt", "r") as fichier_range:
        range = fichier_range.read()

# Import flop file.  Must be in PIO format with weights.
with open("KQJT.txt", "r") as fichier_flop:
        flops_file = fichier_flop.read()


# Function to decompose range as combo + freq of the combo in the range.
def decompose_range(range):
    range_decompose = range.split(sep=",")
    return range_decompose


# Function to decompose flop cards and remove suits.
def decompose_flops():
    flop_decompose = flops_file.split(sep="\n")
    flop_decompose = [flops[0] + flops[2] + flops[4] for flops in flop_decompose]
    flop_set = set(flop_decompose)
    return flop_set

# Decomposition of range as combo + freq of the combo in the range.
liste_range = decompose_range(range)

"""Verification of Range decomposition
print(liste_range)"""

# Decomposition of flop cards without suit.
liste_flops = decompose_flops()

"""Verification of flop decomposition
print(liste_flops)"""


# Balance frequencies for suited and offsuit combos.
def liste_finale(liste_range):
    liste_finale = list()
    for i, combos in enumerate(liste_range):
        if len(combos) == 2 and combos[0] != combos[1]:
            liste_finale.append(liste_range[i] + "o:1")
            liste_finale.append(liste_range[i] + "s:1")
        elif len(combos) == 2 and combos[0] == combos[1]:
            liste_finale.append(liste_range[i] + "p:1")
        elif len(combos) == 3:
            liste_finale.append(liste_range[i] + ":1")
        elif combos[0] == combos[1] and combos[2] == ":":
            add_list_range = liste_range[i]
            add_list_range = add_list_range[:2] + "p" + add_list_range[2:]
            liste_finale.append(add_list_range)
        else:
            liste_finale.append(liste_range[i])
    return liste_finale

liste_finale = liste_finale(liste_range)

"""Verification of range frequencies"""
print(liste_finale)

# Decomposition of combos as absolute freq.
combo_freq = dict(x.split(":") for x in liste_finale)
for cle, valeur in combo_freq.items():
    combo_freq[cle] = float(valeur)

"""Verification of combos decomposition
print(combo_freq)"""

# Test of a single flop.
"""
#Sélection du flop
flop1 = str("789")
print ("flop converti", flop1)
"""


# Convert flop as numeric value.
def flop_convert(flop):
    liste_carte = flop.strip()
    liste_finale = list()
    for carte in liste_carte:
        if carte == "A":
            liste_finale.append(14)
        elif carte == "K":
            liste_finale.append(13)
        elif carte == "Q":
            liste_finale.append(12)
        elif carte == "J":
            liste_finale.append(11)
        elif carte == "T":
            liste_finale.append(10)
        else:
            liste_finale.append(int(carte))
    return sorted(liste_finale, reverse=True)


# Convert hand of range as numeric value.
def hand_convert_range(carte1, carte2):
    liste_carte = [carte1, carte2]
    main_finale = [1, 2]
    for i, carte in enumerate(liste_carte):
        if carte == "A":
            main_finale[i] = 14
        elif carte == "K":
            main_finale[i] = 13
        elif carte == "Q":
            main_finale[i] = 12
        elif carte == "J":
            main_finale[i] = 11
        elif carte == "T":
            main_finale[i] = 10
        else:
            main_finale[i] = int(carte)

    return sorted(main_finale, reverse=True)

# Test of conversion
"""
main1 = hand_convert(main1)
print(main1)
"""


# Creation of a final hand with hands and flops.
def board_generator(flop, hand):
    board = list()
    board.extend(flop)
    board.extend(hand)
    board = sorted(board, reverse=True)
    return board

# Test of final hand.
"""
board = board_generator(flop1,main1)
print(board)
"""


# Determine if the final hand has a pair that wasn't in the flop.
def paired_board(flop, hand):
    paired = False
    board = board_generator(flop, hand)
    if len(board) > len(set(board)) and len(flop) == len(set(flop)):
        paired = True

    return paired


# Determine if the flop has a pair.
def paired_flop(flop):
    flop_paired = False
    if len(flop) > len(set(flop)):
        flop_paired = True

    return flop_paired


# Determine if the final hand is a straight.
def is_straight(board):
    straight = True
    i = 0
    while i < 4:
        if board[i] - board[i + 1] != 1:
            straight = False
            return straight
        i += 1
    if board[0] == 14:
        k = 0
        board2 = [board[1], board[2], board[3], board[4], 1]
        while k < 4:
            if board2[k] - board2[k + 1] != 1:
                straight = False
                return straight
            k += 1

    return straight


# Determine if the final hand is an open ended straight draw with both cards.
def is_oesd(board, flop, hand):
    oesd = False
    if not is_one_card_oesd(flop, hand) and not paired_board(flop, hand):
        i = 0
        compte = 0
        while i < 4:
            if board[i] - board[i + 1] == 1:
                compte += 1
            i += 1
        if compte == 3 and board[1] - board[2] == 1 and board[2] - board[3] == 1:
            oesd = True
        if compte == 3 and paired_flop(flop):
                oesd = True
    if board[0] == 14:
        oesd == False

    return oesd


# Determine if a final hand is a one card open ended straight draw.
def is_one_card_oesd(flop, hand):
    board = board_generator(flop, hand)
    one_card_oesd = False
    if hand[0] - hand[1] > 1 and is_straight(board) == False:
        board1 = list()
        board1.extend(flop)
        board1.append(hand[0])
        board1.sort(reverse=True)
        i = 0
        while i < 3:
            if board1[i] - board1[i + 1] == 1:
                one_card_oesd = True
                i += 1
                continue
            else:
                one_card_oesd = False
                break
        if not one_card_oesd:
            board2 = list()
            board2.extend(flop)
            board2.append(hand[1])
            board2.sort(reverse=True)
            j = 0

            while j < 3:
                if board2[j] - board2[j + 1] == 1:
                    one_card_oesd = True
                    j += 1
                    continue
                else:
                    one_card_oesd = False
                    break
    else:
        one_card_oesd = False
    return one_card_oesd


# Determine if the final hand is a pair + open ended straight draw.
def is_paired_oesd(board, flop):
    is_paired_oesd = False
    i = 0
    compte = 0
    if is_oesd:
        return is_paired_oesd
    if flop[0] == flop[1] or flop[1] == flop[2]:
        return is_paired_oesd
    flop_reduit = list(dict.fromkeys(board))
    if len(flop_reduit) > 3:
        while i < 3:
            if flop_reduit[i] - flop_reduit[i + 1] == 1:
                compte += 1
                i += 1
            else:
                break
        if compte == 3:
            is_paired_oesd = True

    return is_paired_oesd


# Determine if the final hand is a gutshot with both cards.
def is_gs(flop, hand):
    gs = False
    board = board_generator(flop, hand)
    if not is_one_card_gs(flop, hand):
        i = 0
        j = 0
        compte = 0
        while i < 4:
            if board[i] - board[i + 1] == 2:
                if i == 0 and board[i + 1] - board[i + 2] == 1 and board[i + 2] - board[i + 3] == 1:
                    gs = True
                if i == 1 and board[i - 1] - board[i] == 1 and board[i + 1] - board[i + 2] == 1:
                    gs = True
                if i == 1 and board[i + 2] - board[i + 3] == 1 and board[i + 1] - board[i + 2] == 1:
                    gs = True
                if i == 2 and board[i - 1] - board[i] == 1 and board[i + 1] - board[i + 2] == 1:
                    gs = True
                if i == 2 and board[i - 2] - board[i - 1] == 1 and board[i - 1] - board[i] == 1:
                    gs = True
                if i == 3 and board[i - 2] - board[i - 1] == 1 and board[i - 1] - board[i] == 1:
                    gs = True
            i += 1
        # Case of a gutshot with Ace as high card.
        if board[0] == 14:
            if not paired_board(flop, hand):
                compte = 0
                while j < 3:
                    if board[j] - board[j + 1] == 1:
                        compte += 1
                    j += 1
            if compte == 3:
                gs = True
            k = 0
            # Case of a gutshot with ace as low card.
            if not gs:
                board2 = [board[1], board[2], board[3], board[4], 1]
                while k < 4:
                    if board2[k] - board2[k + 1] == 2:
                        if k == 0 and board2[k + 1] - board2[k + 2] == 1 and board2[k + 2] - board2[k + 3] == 1:
                            gs = True
                        if k == 1 and board2[k - 1] - board2[k] == 1 and board2[k + 1] - board2[k + 2] == 1:
                            gs = True
                        if k == 1 and board2[k + 2] - board2[k + 3] == 1 and board2[k + 1] - board2[k + 2] == 1:
                            gs = True
                        if k == 2 and board2[k - 1] - board2[k] == 1 and board2[k + 1] - board2[k + 2] == 1:
                            gs = True
                        if k == 2 and board2[k - 2] - board2[k - 1] == 1 and board2[k - 1] - board2[k] == 1:
                            gs = True
                        if k == 3 and board2[k - 2] - board2[k - 1] == 1 and board2[k - 1] - board2[k] == 1:
                            gs = True
                    k += 1
                    if not paired_board(flop, hand):
                        compte = 0
                        while j < 3:
                            if board2[j] - board2[j + 1] == 1:
                                compte += 1
                            j += 1
                        if compte == 3:
                            gs = True
        # Case of paired flops.
    if paired_flop(flop):
        if board[0] - board[1] == 2 and board[1] - board[2] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[0] - board[1] == 2 and board[2] - board[3] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[0] - board[1] == 2 and board[1] - board[2] == 1 and board[2] - board[3] == 1:
            gs = True
        if board[1] - board[2] == 2 and board[2] - board[3] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[1] - board[2] == 2 and board[0] - board[1] == 1 and board[2] - board[3] == 1:
            gs = True
        if board[1] - board[2] == 2 and board[0] - board[1] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[2] - board[3] == 2 and board[0] - board[1] == 1 and board[1] - board[2] == 1:
            gs = True
        if board[2] - board[3] == 2 and board[1] - board[2] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[2] - board[3] == 2 and board[0] - board[1] == 1 and board[3] - board[4] == 1:
            gs = True
        if board[3] - board[4] == 2 and board[0] - board[1] == 1 and board[1] - board[2] == 1:
            gs = True
        if board[3] - board[4] == 2 and board[0] - board[1] == 1 and board[2] - board[3] == 1:
            gs = True
        if board[3] - board[4] == 2 and board[1] - board[2] == 1 and board[2] - board[3] == 1:
            gs = True

    return gs


# Determine if a hand is a one card gutshot.
def is_one_card_gs(flop, hand):
    one_card_gs = False
    board1 = list()
    board1.extend(flop)
    board1.append(hand[0])
    board1.sort(reverse=True)
    compte1 = 0
    i = 0
    board = board_generator(flop, hand)
    if not is_straight(board) and not is_one_card_oesd(flop, hand):
        while i < 3:
            if board1[i] - board1[i + 1] == 1:
                compte1 += 1
            i += 1
        if compte1 == 2:
            if board1[0] - board1[1] == 2 or board1[1] - board1[2] == 2 or board1[2] - board1[3] == 2:
                one_card_gs = True
                return one_card_gs
        else:
            one_card_gs = False

        board2 = list()
        board2.extend(flop)
        board2.append(hand[1])
        board2.sort(reverse=True)
        compte2 = 0
        j = 0
        while j < 3:
            if board2[j] - board2[j + 1] == 1:
                compte2 += 1
            j += 1
        if compte2 == 2:
            if board2[0] - board2[1] == 2 or board2[1] - board2[2] == 2 or board2[2] - board2[3] == 2:
                one_card_gs = True
                return one_card_gs
        else:
            one_card_gs = False
            return one_card_gs
    return one_card_gs


# Determine if the final hand is a double gutshot.
def is_double_gs(flop, hand):
    double_gs = False
    one_card_gs1 = False
    one_card_gs2 = False
    board1 = list()
    board1.extend(flop)
    board1.append(hand[0])
    board1.sort(reverse=True)
    compte1 = 0
    i = 0
    board = board_generator(flop, hand)
    if not is_straight(board):
        while i < 3:
            if board1[i] - board1[i + 1] == 1:
                compte1 += 1
            i += 1
        if compte1 == 2:
            if board1[0] - board1[1] == 2 or board1[1] - board1[2] == 2 or board1[2] - board1[3] == 2:
                one_card_gs1 = True
        else:
            one_card_gs1 = False

        board2 = list()
        board2.extend(flop)
        board2.append(hand[1])
        board2.sort(reverse=True)
        compte2 = 0
        j = 0
        while j < 3:
            if board2[j] - board2[j + 1] == 1:
                compte2 += 1
            j += 1
        if compte2 == 2:
            if board2[0] - board2[1] == 2 or board2[1] - board2[2] == 2 or board2[2] - board2[3] == 2:
                one_card_gs2 = True
        else:
            one_card_gs2 = False
    if one_card_gs1 and one_card_gs2:
        double_gs = True
    return double_gs


# Determine if the final hand is a pair + gutshot.
def is_paired_gs(board, flop, hand):
    paired_gs = False
    compte = 0
    i = 0
    if paired_board(flop, hand):
        while i < 4:
            if board[i] - board[i + 1] == 1:
                compte += 1
            i += 1
        if compte == 2:
            if board[0] - board[1] == 2 or board[1] - board[2] == 2 or board[2] - board[3] == 2 or board[3] - board[4] == 2:
                paired_gs = True

    return paired_gs


# Count the number of draws.
# Rajouter return le type direct quand il le trouve et break pour optimiser
def count_draw(flop, hand, board):
    connexion = {"straight": 0, "oesd": 0, "one_card_oesd": 0, "paired_oesd": 0, "gs": 0, "one_card_gs": 0, "paired_gs": 0, "double_gs": 0}

    if is_straight(board):
        connexion["straight"] += 1
        return connexion
    if is_double_gs(flop, hand):
        connexion["double_gs"] += 1
        return connexion
    if is_paired_gs(board, flop, hand):
        connexion["paired_gs"] += 1
        return connexion
    if is_paired_oesd(board, flop):
        connexion["paired_oesd"] += 1
        return connexion
    if is_one_card_gs(flop, hand):
        connexion["one_card_gs"] += 1
        return connexion
    if is_one_card_oesd(flop, hand):
        connexion["one_card_oesd"] += 1
        return connexion
    if is_oesd(board, flop, hand):
        connexion["oesd"] += 1
        return connexion
    if is_gs(flop, hand):
        connexion["gs"] += 1

    return connexion


# Adjust the count of each draw with combos and range frequencies.
def ponderation_combo(combo_freq):
    for combo_type, nombre_de_combo in combo_freq.items():
        print(combo_type)
        if combo_type[2] == "p":
            combo_freq[combo_type] = nombre_de_combo * 6
        elif combo_type[2] == "s":
            combo_freq[combo_type] = nombre_de_combo * 4
        elif combo_type[2] == "o":
            combo_freq[combo_type] = nombre_de_combo * 12
    return combo_freq

liste_pondere = ponderation_combo(combo_freq)
print(liste_pondere)

# Constants of importance of draws.
# It will multiply the number of each draws with this number to better reflect
# the impact of the draw on the equity of the range.
# Thinking process is for exemple that you won't extract as much value when you
# hit a one card oesd than a regular oesd.
PONDERATION = {"straight": 10, "oesd": 5, "one_card_oesd": 3, "paired_oesd": 3, "gs": 2, "one_card_gs": 1, "paired_gs": 1, "double_gs": 10}


# Final result of connections of the range on a given flop.
def analyse_hands(liste_pondere, flop, ponderation):
    connexion = dict()
    compte_final2 = dict()
    compte_final = {"straight": 0, "oesd": 0, "one_card_oesd": 0, "paired_oesd": 0, "gs": 0, "one_card_gs": 0, "paired_gs": 0, "double_gs": 0}
    score_final = {"straight": 0.0, "oesd": 0.0, "one_card_oesd": 0.0, "paired_oesd": 0.0, "gs": 0.0, "one_card_gs": 0.0, "paired_gs": 0.0, "double_gs": 0.0}
    for combo_type, nombre_de_combo in liste_pondere.items():
        hand = hand_convert_range(combo_type[0], combo_type[1])
        board = board_generator(flop, hand)
        connexion = count_draw(flop, hand, board)
        print("hand: ", hand, "\n" "board :", board, "\n", "result", connexion)  # Verification of connectivity of combos.
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
    flop = flop_convert(flops)
    score_flop[flops] = analyse_hands(liste_pondere, flop, PONDERATION)

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
