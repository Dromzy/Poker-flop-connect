## What it does?
This script analyze a poker hand range against any flops subset by calculating connectivity.
It calculates a connection score for each flop based on the number of draws created with all the hands of the subset.
Each hand can only form a single draw at a time with this system of priority.
```
        ("straight", lambda: is_straight(board)),
        ("paired_oesd", lambda: is_paired_oesd(board, flop, hand)),
        ("one_card_oesd", lambda: is_one_card_oesd(flop, hand)),
        ("oesd", lambda: is_just_oesd(board, flop, hand)),
        ("double_gs", lambda: is_double_gs(flop, hand)),
        ("paired_gs", lambda: is_paired_gs(board, flop, hand)),
        ("one_card_gs", lambda: is_one_card_gs(flop, hand)),
        ("gs", lambda: is_gs(flop, hand))
```

The priority is determined by the score of the draw in ponderation and mutual exclusions
(paired_oesd is a subset of one_card_oesd which is a subsetof oesd)

## Usage

Edit the ponderation of each draw to calculate the score
Run the script

This is the example with a sample range and flop:
```python
python .\connexion_flop.py "range.txt" "flops.txt"
```

## Unit tests

```python
python .\tests.py    
```
