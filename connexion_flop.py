import os
import sys
import pprint
import math
import unittest
from collections import defaultdict
from utils import *

# Constants for draw multipliers
PONDERATION = {
    "straight": 10,
    "oesd": 5,
    "one_card_oesd": 3,
    "paired_oesd": 3,
    "gs": 2,
    "one_card_gs": 1,
    "paired_gs": 1,
    "double_gs": 10
}

def analyse_hands(adjusted_combos_freq, flop, ponderation):
    """
    Analyzes the connections of a range on a given flop.

    Parameters:
    - adjusted_combos_freq (dict): A dictionary where keys are combo types and values are their adjusted frequencies.
    - flop (list): The current flop cards.
    - ponderation (dict): A dictionary containing score for each draw type.

    Returns:
    - dict: A dictionary with the final scores for each draw type.
    """
    total_draws = defaultdict(float)

    for combo_type, combo_count in adjusted_combos_freq.items():
        # Convert combo type to a hand
        hand = convert_hand(combo_type[0], combo_type[1])

        # Generate the full board with the current hand
        board = generate_board(flop, hand)

        # Count the draws on the current board
        draw_counts = count_draw(flop, hand, board)

        # Accumulate the weighted draw counts
        for draw_type, count in draw_counts.items():
            total_draws[draw_type] += count * combo_count

    # Apply ponderation to each draw type and round up
    final_scores = {draw_type: math.ceil(total_draws[draw_type] * ponderation.get(draw_type, 1))
                   for draw_type in ponderation}

    return final_scores

def main(range_file="range-test.txt", flop_file="flops-test.txt"):
    """
    Main function to analyze poker hand ranges against flops and calculate connection scores.

    Parameters:
    - range_file (str): Path to the range file in PIO format.
    - flop_file (str): Path to the flop file in PIO format.
    
    Returns:
    - list: Sorted list of flop results based on connection scores.
    """
    # Read range and flop files
    with open(range_file, "r") as file_range:
        range_data = file_range.read()

    with open(flop_file, "r") as file_flop:
        flops_data = file_flop.read()

    # Decompose range into combos
    range_combos = decompose_range(range_data)

    # Decompose flops and remove suits
    flop_decomposed = [flop_line[0] + flop_line[2] + flop_line[4] for flop_line in flops_data.split("\n") if flop_line.strip()]
    unique_flops = set(flop_decomposed)

    # Expand combos in PIO expanded form
    expanded_combos = expand_combos_range(range_combos)

    # Parse combo frequencies
    combos_freq = {combo.split(":")[0]: float(combo.split(":")[1]) for combo in expanded_combos}

    # Apply ponderation to combos
    adjusted_combos_freq = ponderation_combo(combos_freq)

    # Analyze each flop
    flop_scores = {}
    for flop_str in unique_flops:
        flop = convert_flop(flop_str)
        flop_scores[flop_str] = analyse_hands(adjusted_combos_freq, flop, PONDERATION)

    # Calculate final connection scores per flop
    final_flop_scores = {}
    for flop_str, scores in flop_scores.items():
        total_score = sum(scores.values())
        final_flop_scores[flop_str] = total_score

    # Sort flops based on their final scores
    sorted_flops = sorted(final_flop_scores.items(), key=lambda item: item[1])

    pprint.pprint(sorted_flops, width=1)
    return sorted_flops

if __name__ == "__main__":
    range_file = sys.argv[1] if len(sys.argv) > 1 else "range-test.txt"
    flop_file = sys.argv[2] if len(sys.argv) > 2 else "flops-test.txt"
    main(range_file, flop_file)
