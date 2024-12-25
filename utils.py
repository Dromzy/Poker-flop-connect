from itertools import combinations

# Function to decompose range as combo + freq of the combo in the range.
def decompose_range(range):
    range_decompose = range.split(sep=",")
    return range_decompose

    # Balance frequencies for suited and offsuit combos.
def expand_combos_range(liste_range):
    range_combos_expanded = []
    for combos in liste_range:
        if len(combos) == 2:
            if combos[0] != combos[1]:
                range_combos_expanded.append(f"{combos}o:1")
                range_combos_expanded.append(f"{combos}s:1")
            else:
                range_combos_expanded.append(f"{combos}p:1")
        elif len(combos) == 3 and ":" not in combos:
            range_combos_expanded.append(f"{combos}:1")
        elif len(combos) > 2 and combos[0] == combos[1] and combos[2] == ":":
            prefix = combos[:2] + "p"
            range_combos_expanded.append(f"{prefix}{combos[2:]}")
        else:
            range_combos_expanded.append(combos)
    return range_combos_expanded

# Adjust the count of each draw with combos and range frequencies.
def ponderation_combo(combos_freq):
    for combo_type, nombre_de_combo in combos_freq.items():
        if combo_type[2] == "p":
            combos_freq[combo_type] = nombre_de_combo * 6
        elif combo_type[2] == "s":
            combos_freq[combo_type] = nombre_de_combo * 4
        elif combo_type[2] == "o":
            combos_freq[combo_type] = nombre_de_combo * 12
    return combos_freq

# Utility function to convert card values.
def convert_card_value(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 11
    if card == "T":
        return 10
    return int(card)

# Convert flop cards to numeric values.
def convert_flop(flop):
    return sorted([convert_card_value(c) for c in flop], reverse=True)

# Convert hand to numeric values.
def convert_hand(card1,card2):
    return sorted([convert_card_value(card1), convert_card_value(card2)], reverse=True)

# Generate a board combining flop and hand.
def generate_board(flop, hand):
    return sorted(flop + hand, reverse=True)

# Determine if the final hand has a pair that wasn't in the flop.
def is_paired_board(flop, hand):
    board = generate_board(flop, hand)
    return len(board) > len(set(board)) and len(flop) == len(set(flop))

# Determine if the flop has a pair.
def is_paired_flop(flop):
    return len(flop) > len(set(flop))

def is_straight(board):
    # Check for standard straight
    if all(board[i] - board[i + 1] == 1 for i in range(len(board) - 1)):
        return True

    # Check for Ace-low straight (A, 5, 4, 3, 2)
    if board[0] == 14 and board[-4:] == [5, 4, 3, 2]:
        return True

    return False

def is_wrong_oesd_A_high(board):
    if 14 in board and 13 in board and 12 in board and 11 in board:
        return True
    return False

def is_oesd(board):
    if is_wrong_oesd_A_high(board) or is_straight(board):
        return False
    return any(
        all(board[i + j] - board[i + j + 1] == 1 for j in range(3))
        for i in range(len(board) - 3)
    )


# Determine if a final hand is just a one card open ended straight draw.
def is_one_card_oesd(flop, hand):
    if is_paired_board(flop, hand) or is_paired_flop(flop) or is_straight(generate_board(flop, hand)) or is_wrong_oesd_A_high(flop + hand):
        return False

    # Check OESD contribution from a single card
    def contributes_to_oesd(card, flop):
        extended_board = sorted(flop + [card], reverse=True)
        gaps = [extended_board[i] - extended_board[i + 1] for i in range(len(extended_board) - 1)]
        return gaps.count(1) == 3

    # Check if either card in the hand contributes to an OESD
    return contributes_to_oesd(hand[0], flop) or contributes_to_oesd(hand[1], flop)

# Determine if the final hand is just an open ended straight draw with both cards.
def is_just_oesd(board, flop, hand):
    if is_one_card_oesd(flop, hand) or is_paired_board(flop, hand) or is_straight(board) or is_wrong_oesd_A_high(board):
        return False

    return any(
        all(board[i + j] - board[i + j + 1] == 1 for j in range(3))
        for i in range(len(board) - 3)
    )

# Determine if the final hand is a pair + open ended straight draw with both cards of the hand.
def is_paired_oesd(board, flop, hand):
    if is_one_card_oesd(flop, hand) or is_paired_flop(flop) or is_straight(board) or is_wrong_oesd_A_high(board):
        return False

    if is_paired_board(flop,hand):
        unique_board = sorted(set(board), reverse=True)
        gaps = [unique_board[i] - unique_board[i + 1] for i in range(len(unique_board) - 1)]
        if gaps.count(1) == 3:
            return True

    return False

# Determine if a subset of 4 cards has a gutshot
# A valid gutshot: exactly one gap of 2, and all other gaps of 1.
# There are 3 gaps in a 4-card sequence. One must be 2, two must be 1.
def has_gutshot(cards4):
    # cards4 should be sorted in descending order
    gaps = [cards4[i] - cards4[i+1] for i in range(len(cards4)-1)]
    return gaps.count(2) == 1 and gaps.count(1) == 2

# Helper function to count how many 4-card subsets form a gutshot
def count_gs(cards):
    cnt = 0
    for subset in combinations(cards, 4):
        sub = sorted(subset, reverse=True)
        if has_gutshot(sub):
            cnt += 1
    return cnt

# Determine if the final hand is a gutshot with both cards.
def is_gs(flop, hand):
    board = generate_board(flop, hand)
    if is_oesd(board) or is_straight(board) or is_paired_board(flop, hand) or is_one_card_gs(flop,hand):
        return False
    if is_paired_flop(flop):
        board = list({k: None for k in board}.keys())

    gs_count = count_gs(board)

    # If an Ace is present, consider Ace as low and re-check
    if 14 in board:
        low_board = sorted([1 if c == 14 else c for c in board], reverse=True)
        gs_count += count_gs(low_board)

    return gs_count == 1

# Determine if a hand is a one card gutshot.
def is_one_card_gs(flop, hand):
    board = generate_board(flop, hand)
    if is_straight(board) or is_oesd(board) or is_paired_board(flop, hand) or is_paired_flop(flop) or is_one_card_oesd(flop, hand):
        return False

    def check_gutshot_with_card(card, flop_cards):
        four_cards = sorted(flop_cards + [card], reverse=True)
        return has_gutshot(four_cards)

    def one_card_gutshot_count(flop_cards, hand_cards):
        count = 0
        if check_gutshot_with_card(hand_cards[0], flop_cards):
            count += 1
        if check_gutshot_with_card(hand_cards[1], flop_cards):
            count += 1
        return count

    gs_count = one_card_gutshot_count(flop, hand)

    # If Ace present, consider Ace as low and re-check
    if 14 in board:
        low_flop = sorted([1 if c == 14 else c for c in flop], reverse=True)
        low_hand = [1 if c == 14 else c for c in hand]
        gs_count += one_card_gutshot_count(low_flop, low_hand)

    return gs_count == 1


# Determine if the final hand is a double gutshot.
def is_double_gs(flop, hand):
    board = generate_board(flop, hand)
    if is_oesd(board) or is_straight(board) or is_paired_board(flop, hand) or is_paired_flop(flop) or is_one_card_gs(flop,hand):
        return False

    gs_count = count_gs(board)
    # If an Ace is present, consider Ace as low and re-check
    if 14 in board:
        low_board = sorted([1 if c == 14 else c for c in board], reverse=True)
        gs_count = count_gs(low_board)

    return gs_count == 2


# Determine if the final hand is a pair + gutshot.
def is_paired_gs(board, flop, hand):
    high_gs = has_gutshot(list({k: None for k in board}.keys()))
    low_gs = False
    if 14 in board:
        low_board = sorted([1 if c == 14 else c for c in board], reverse=True)
        low_gs = has_gutshot(list({k: None for k in low_board}.keys()))

    return is_paired_board(flop, hand) and (high_gs or low_gs)


# Count the number of draws.
def count_draw(flop, hand, board):
    connexion = {"straight": 0, "oesd": 0, "one_card_oesd": 0, "paired_oesd": 0, "gs": 0, "one_card_gs": 0, "paired_gs": 0, "double_gs": 0}

    draw_checks = [
        ("straight", lambda: is_straight(board)),
        ("paired_oesd", lambda: is_paired_oesd(board, flop, hand)),
        ("one_card_oesd", lambda: is_one_card_oesd(flop, hand)),
        ("oesd", lambda: is_just_oesd(board, flop, hand)),
        ("double_gs", lambda: is_double_gs(flop, hand)),
        ("paired_gs", lambda: is_paired_gs(board, flop, hand)),
        ("one_card_gs", lambda: is_one_card_gs(flop, hand)),
        ("gs", lambda: is_gs(flop, hand))
    ]

    # Iterate through the draw checks in order of priority
    for key, check in draw_checks:
        if check():
            connexion[key] = 1
            return connexion  # Return immediately after finding the first matching draw type

    return connexion