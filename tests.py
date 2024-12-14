import unittest
from utils import *
from connexion_flop import main

class BaseTest(unittest.TestCase):

    def setUp(self):
        # File paths for range and flops
        self.range_file = "./range-test.txt"
        self.flop_file = "./flops-test.txt"


# Define unit tests.
class TestEndToEnd(BaseTest):
    def test_end_to_end_result(self):
        expected_result = [
            ('T44', 0.0), ('KK7', 0), ('Q66', 0), ('JJ3', 0), ('Q77', 0), ('TT4', 0), ('TT5', 0),
            ('J66', 0), ('JJ2', 0), ('QQ5', 0), ('Q55', 0), ('JJ4', 0), ('KK8', 0), ('Q33', 0),
            ('K33', 0), ('J55', 0), ('KK2', 0), ('K82', 0), ('K44', 0), ('JJ5', 0), ('J22', 0),
            ('JJ6', 0), ('TT3', 0), ('TT2', 0), ('KKK', 0), ('T22', 0), ('K55', 0), ('QQ3', 0),
            ('QQ7', 0), ('KK3', 0), ('T55', 0), ('K83', 0), ('Q22', 0), ('TTT', 0), ('KK6', 0),
            ('K66', 0), ('K77', 0), ('Q44', 0), ('QQ6', 0), ('K88', 0), ('T33', 0), ('JJJ', 0),
            ('QQQ', 0), ('Q72', 0), ('K72', 0), ('J44', 0), ('KK4', 0), ('J33', 0), ('K22', 0),
            ('QQ2', 0), ('QQ4', 0), ('KK5', 0), ('J64', 2), ('K52', 2), ('J52', 2), ('T52', 2),
            ('Q52', 2), ('Q64', 2), ('K62', 3), ('K85', 3), ('Q62', 3), ('J62', 3), ('Q74', 4),
            ('Q63', 4), ('K53', 4), ('Q75', 4), ('K74', 4), ('K75', 4), ('K63', 4), ('J53', 4),
            ('J63', 4), ('T53', 4), ('Q53', 4), ('Q73', 5), ('K73', 5), ('Q42', 5), ('T42', 5),
            ('J42', 5), ('K84', 5), ('K42', 5), ('K64', 6), ('T75', 6), ('T72', 6), ('T66', 6),
            ('TT6', 6), ('K86', 8), ('T62', 8), ('T77', 9), ('T83', 9), ('JJ7', 9), ('T74', 9),
            ('T82', 9), ('TT7', 9), ('J72', 9), ('TT8', 9), ('T88', 9), ('J77', 9), ('T85', 10),
            ('T63', 10), ('T73', 11), ('J83', 12), ('J82', 12), ('Q83', 13), ('J74', 13), ('Q88', 13),
            ('KQQ', 13), ('Q82', 13), ('T64', 13), ('KJJ', 13), ('QQ8', 13), ('J73', 14), ('J85', 15),
            ('QJJ', 15), ('J86', 15), ('J84', 16), ('Q85', 16), ('Q84', 17), ('J88', 17), ('JJ8', 17),
            ('KK9', 18), ('K99', 18), ('K94', 18), ('K92', 18), ('K93', 18), ('KJ4', 19), ('T84', 19),
            ('KJ3', 19), ('KJ5', 19), ('KJ2', 19), ('KJ6', 19), ('T54', 20), ('KJ8', 21), ('K95', 21),
            ('K96', 21), ('KKJ', 22), ('J75', 23), ('T43', 23), ('QQT', 24), ('T32', 24), ('KQ2', 25),
            ('JJ9', 27), ('T86', 27), ('Q54', 28), ('Q93', 28), ('Q92', 28), ('QQJ', 28), ('Q94', 28),
            ('KQ5', 29), ('Q65', 30), ('T65', 30), ('KQ3', 30), ('Q96', 31), ('TT9', 31), ('Q97', 31),
            ('J96', 32), ('J92', 32), ('J93', 32), ('Q95', 32), ('J94', 32), ('KKQ', 32), ('Q43', 32),
            ('KQ4', 32), ('Q32', 33), ('KQ7', 34), ('KQ6', 35), ('J99', 35), ('QJ2', 35), ('Q99', 35),
            ('QQ9', 35), ('Q86', 36), ('QT5', 36), ('QT8', 36), ('QT4', 36), ('QT2', 36), ('QT3', 36),
            ('QJ5', 37), ('QJ4', 38), ('JJT', 38), ('QJ3', 38), ('Q76', 38), ('T92', 38), ('QT7', 39),
            ('J95', 41), ('J54', 41), ('QJ6', 41), ('T93', 42), ('T99', 42), ('T94', 42), ('KJ7', 43),
            ('J65', 43), ('J43', 44), ('QTT', 44), ('J97', 45), ('J32', 45), ('T95', 46), ('T76', 48),
            ('K54', 49), ('KT2', 50), ('KT5', 50), ('KT3', 50), ('KT4', 50), ('K97', 51), ('QT6', 52),
            ('QJ7', 53), ('K43', 53), ('K65', 53), ('K32', 55), ('KT6', 55), ('KT7', 55), ('KKT', 56),
            ('KTT', 56), ('KJ9', 56), ('KQ8', 57), ('JT2', 58), ('QJ8', 59), ('T96', 61), ('JT5', 61),
            ('KT8', 61), ('JT4', 61), ('JT3', 62), ('K76', 63), ('J76', 63), ('JTT', 68), ('Q87', 69),
            ('T97', 69), ('JT6', 69), ('KQ9', 71), ('T87', 72), ('K87', 75), ('Q98', 77), ('J87', 78),
            ('JT8', 79), ('JT7', 84), ('J98', 103), ('QJ9', 103), ('QT9', 113), ('K98', 113), ('KT9', 115),
            ('KQJ', 123), ('T98', 146), ('QJT', 159), ('KQT', 160), ('JT9', 185), ('KJT', 194)
        ]
        result = main()
        for item in expected_result:
            self.assertIn(item, result)

class TestRangeFunctions(BaseTest):
    def test_range_expansion(self):
        range_content = (
            "AA:0.1336,TT:0.2041,99:0.786,88:0.9413,77:0.8393,66:0.7541,55:0.475,44:0.3256,33:0.2895,22:0.1734,"
            "AQs:0.8895,AQo:0.6609,AJs:1,AJo:0.3617,ATs:1,A9s:0.7514,A8s:0.0773,A5s:0.3121,A4s:0.1498,"
            "KQs:1,KQo:0.3118,KJs:1,KTs:0.9878,K9s:0.418,QJs:0.7702,QTs:0.4364,JTs:0.931,T9s:0.6015,"
            "T8s:0.004,98s:0.436,87s:0.2169,76s:0.235,65s:0.2702,54s:0.3195"
        )
        expected_result = [
            'AAp:0.1336', 'TTp:0.2041', '99p:0.786', '88p:0.9413', '77p:0.8393', '66p:0.7541', '55p:0.475',
            '44p:0.3256', '33p:0.2895', '22p:0.1734', 'AQs:0.8895', 'AQo:0.6609', 'AJs:1', 'AJo:0.3617', 'ATs:1',
            'A9s:0.7514', 'A8s:0.0773', 'A5s:0.3121', 'A4s:0.1498', 'KQs:1', 'KQo:0.3118', 'KJs:1', 'KTs:0.9878',
            'K9s:0.418', 'QJs:0.7702', 'QTs:0.4364', 'JTs:0.931', 'T9s:0.6015', 'T8s:0.004', '98s:0.436',
            '87s:0.2169', '76s:0.235', '65s:0.2702', '54s:0.3195'
        ]
        
        # Decompose the range and expand it
        range_combos = decompose_range(range_content)
        expanded_range = expand_combos_range(range_combos)

        # Assert the expanded range matches the expected result
        self.assertEqual(expanded_range, expected_result)

class TestPairedBoard(BaseTest):
    def test_paired_board(self):
        # Case 1: Board has a pair not present in the flop
        flop = [2, 5, 8]
        hand = [9, 8]
        self.assertTrue(is_paired_board(flop, hand))  # Pair created by 8 in hand
        
        # Case 2: No pair on the board
        flop = [3, 6, 10]
        hand = [9, 8]
        self.assertFalse(is_paired_board(flop, hand))  # No pair anywhere
        
        # Case 3: Flop already has a pair
        flop = [7, 7, 2]
        hand = [9, 5]
        self.assertFalse(is_paired_board(flop, hand))  # Flop already paired, not new
        
        # Case 4: Hand creates a new pair
        flop = [4, 7, 10]
        hand = [9, 4]
        self.assertTrue(is_paired_board(flop, hand))  # Pair created by 4 in hand

class TestPairedFlop(BaseTest):
    def test_paired_flop(self):
        # Test case: Flop with a pair
        flop = ['K', 'K', 'Q']
        self.assertTrue(is_paired_flop(flop))  # Expected: True

        # Test case: Flop without a pair
        flop = ['K', 'Q', 'J']
        self.assertFalse(is_paired_flop(flop))  # Expected: False

        # Test case: Flop with all identical cards
        flop = ['K', 'K', 'K']
        self.assertTrue(is_paired_flop(flop))  # Expected: True

        # Test case: Flop with different numeric cards
        flop = ['3', '7', '9']
        self.assertFalse(is_paired_flop(flop))  # Expected: False

class TestConnectivityScore(BaseTest):
    def test_straight_detection(self):
        self.assertTrue(is_straight([14, 13, 12, 11, 10]))  # A-K-Q-J-T
        self.assertTrue(is_straight([14, 5, 4, 3, 2]))       # 5-4-3-2-A
        self.assertFalse(is_straight([14, 13, 12, 11, 9]))  # A-K-Q-J-9


class TestIsOESD(BaseTest):
    def test_open_ended_straight_draw(self):
        # Cases with straight instead of open-ended straight draw
        self.assertFalse(is_oesd([6, 5, 4, 3, 2]))  # 6-5-4-3-2
        
        # Cases with oesd with only one card
        self.assertTrue(is_oesd([10, 9, 8, 7, 2]))  # T-9-8-7-2
        
        # Case with wrong OESD A high
        self.assertFalse(is_oesd([14, 13, 12, 11, 9]))  # A-K-Q-J-9 no OESD

    def test_just_open_ended_straight_draw(self):
        # Cases with straight instead of open-ended straight draw
        self.assertFalse(is_just_oesd([6, 5, 4, 3, 2], [5, 4, 3], [6, 2]))  # 6-5-4-3-2
        
        # Cases with oesd with only one card
        self.assertTrue(is_just_oesd([10, 9, 8, 7, 2], [8, 7, 2], [10, 9]))  # T-9-8-7-2
        self.assertTrue(is_just_oesd([11, 5, 4, 3, 2], [11, 4, 3], [5, 2]))  # J-5-4-3-2

        # Cases without open-ended straight draw
        self.assertFalse(is_just_oesd([14, 13, 12, 11, 9], [13, 12, 11], [14, 9]))  # A-K-Q-J-9
        self.assertFalse(is_just_oesd([7, 6, 5, 3, 2], [6, 5, 3], [7, 2]))  # 7-6-5-3-2

        # Board is paired
        self.assertTrue(is_just_oesd([7, 7, 6, 5, 4], [7, 7, 5], [6, 4]))  # Paired flop, OESD
        self.assertFalse(is_just_oesd([10, 10, 9, 8, 7], [10, 9, 8], [10, 7]))  # Paired board

        # Edge case with Ace
        self.assertTrue(is_just_oesd([14, 12, 11, 10, 9], [14, 11, 10], [12, 9]))  # A-Q-J-T-9
        self.assertFalse(is_just_oesd([14, 12, 11, 10, 9], [12, 11, 10], [14, 9]))  # A-Q-J-T-9
        self.assertFalse(is_just_oesd([14, 13, 12, 11, 9], [12, 11, 9], [14, 13]))  # A-K-Q-J-9 no OESD


class TestIsOneCardOESD(BaseTest):
    def test_one_card_oesd(self):
        # Cases where one card from the hand contributes to an OESD
        self.assertTrue(is_one_card_oesd([10, 9, 8], [7, 2]))  # 10-9-8 with 7 forms OESD
        self.assertTrue(is_one_card_oesd([9, 8, 7], [10, 2]))  # 9-8-7 with 10 forms OESD
        self.assertTrue(is_one_card_oesd([6, 5, 4], [10, 3]))  # 6-5-4 with 3 forms OESD

        # Case of straight
        self.assertFalse(is_one_card_oesd([9, 8, 7], [10, 6]))  # 10-9-8-7-6 is a complete straight

        # Cases where no OESD is formed
        self.assertFalse(is_one_card_oesd([10, 9, 7], [6, 2]))  # No OESD on 10-9-7 with 6
        self.assertFalse(is_one_card_oesd([9, 8, 6], [10, 5]))  # No OESD on 9-8-6 with 10
        self.assertFalse(is_one_card_oesd([6, 5, 4], [9, 2]))  # No OESD on 6-5-4 with 2

        # Edge case: oesd with two cards
        self.assertFalse(is_one_card_oesd([8, 7, 2], [10, 9]))  # T-9-8-7-2
        self.assertFalse(is_one_card_oesd([11, 4, 3], [5, 2]))  # J-5-4-3-2

        # Edge case: paired flop does not form a one card OESD
        self.assertFalse(is_one_card_oesd([9, 9, 8], [10, 7]))  # Paired flop 9-9-8 with 10 or 7

        # Edge case: A high board
        self.assertFalse(is_one_card_oesd([14, 12, 11], [13, 5]))  # A-K-Q-J-5 no OESD

class TestIsPairedOESD(BaseTest):
    def test_paired_oesd(self):
        # Cases where the hand forms a pair + open-ended straight draw
        self.assertTrue(is_paired_oesd([10, 9, 8, 7, 7], [10, 9, 8], [7, 7]))  # Pair of 7s and 10-9-8-7-7 forms OESD
        self.assertTrue(is_paired_oesd([6, 5, 4, 4, 3], [6, 5, 4], [4, 3]))  # Pair of 4s and 6-5-4-4-3 forms OESD

        # Cases where the hand forms a straight but not a paired OESD
        self.assertFalse(is_paired_oesd([10, 9, 8, 7, 6], [10, 9, 8], [7, 6]))  # 10-9-8-7-6 is a complete straight

        # Cases with no OESD
        self.assertFalse(is_paired_oesd([10, 9, 8, 8, 6], [10, 9, 8], [8, 6]))  # Pair of 8s but no OESD
        self.assertFalse(is_paired_oesd([6, 5, 5, 3, 2], [6, 5, 5], [3, 2]))  # Pair of 5s but no OESD

        # Edge cases
        self.assertFalse(is_paired_oesd([14, 13, 12, 12, 11], [14, 13, 12], [12, 11]))  # Pair of Q but no OESD
        self.assertFalse(is_paired_oesd([14, 13, 12, 12, 11], [14, 12, 11], [13, 12]))  # Pair of Q but no OESD

class TestHasGutshot(BaseTest):
    def test_gutshot_patterns(self):
        # Valid gutshot:
        # Example: 9-8-6-5
        # Gaps: (9-8=1, 8-6=2, 6-5=1)
        # One gap of 2, two gaps of 1 → True
        self.assertTrue(has_gutshot([9, 8, 6, 5]))

        # Another valid gutshot:
        # A(14)-J(11)-T(10)-9
        # Sorted descending: 14-11-10-9
        # Gaps: (14-11=3, 11-10=1, 10-9=1)
        # This is not correct since we need exactly one gap of 2 and two gaps of 1.
        # Hence this should be False.
        self.assertFalse(has_gutshot([14, 11, 10, 9]))

        # Another valid gutshot:
        # 10-9-7-6
        # Gaps: (10-9=1, 9-7=2, 7-6=1)
        # One gap of 2, two gaps of 1 → True
        self.assertTrue(has_gutshot([10, 9, 7, 6]))

        # Not a gutshot - too large gaps:
        # 10-8-5-4
        # Gaps: (10-8=2, 8-5=3, 5-4=1)
        # We have one gap of 2 but also a gap of 3, which is not allowed.
        self.assertFalse(has_gutshot([10, 8, 5, 4]))

        # Not a gutshot - missing the 2-gap:
        # 9-8-7-6
        # Gaps: (9-8=1, 8-7=1, 7-6=1)
        # All gaps of 1 means it's straight-like, not a gutshot.
        self.assertFalse(has_gutshot([9, 8, 7, 6]))

        # Edge case: smallest ranks
        # 5-3-2-1 (Ace low scenario maybe)
        # Gaps: (5-3=2, 3-2=1, 2-1=1)
        # Perfect gutshot pattern, one gap of 2, two gaps of 1
        self.assertTrue(has_gutshot([5, 3, 2, 1]))
        self.assertTrue(has_gutshot([14, 13, 11, 10]))

class TestIsGS(BaseTest):
    def test_oesd_gs(self):
        # Cases of OESD
        self.assertFalse(is_gs([10, 9, 8], [7, 5]))  # 10-9-8-7-5 forms a gutshot (6 needed)

    def test_complete_straight(self):
        # Cases where the board and hand already form a straight
        self.assertFalse(is_gs([10, 9, 8], [7, 6]))  # 10-9-8-7-6 forms a complete straight
        self.assertFalse(is_gs([14, 13, 12], [11, 10]))  # 14-13-12-11-10 forms a complete straight

    def test_one_card_gutshot(self):
        # Cases where no gutshot straight draw is present
        self.assertFalse(is_gs([10, 9, 7], [6, 5]))  # One card Gutshot
        self.assertFalse(is_gs([14, 13, 12], [10, 9]))  # One card Gutshot

    def test_paired_board(self):
        # Cases where the board is paired
        self.assertTrue(is_gs([9, 9, 8], [7, 5]))  # Paired flop 9-9-8 with gutshot
        self.assertFalse(is_gs([9, 8, 7], [8, 5]))  # Unpaired flop 10-10-9 with pair + gutshot

    def test_edge_cases(self):
        # Edge cases with Ace as high card
        self.assertFalse(is_gs([14, 12, 11], [10, 9]))  # A-Q-J-T-9, OESD
        self.assertFalse(is_gs([14, 13, 11], [10, 9]))  # A-K-J-T-9, one card gutshot

        # Edge case with Ace as low card
        self.assertFalse(is_gs([5, 4, 3], [14, 2]))  # 5-4-3-2-A, straight wheel
        self.assertFalse(is_gs([6, 5, 4], [14, 3]))  # 6-5-4-3-A, OESD
        self.assertTrue(is_gs([8, 5, 4], [14, 3]))  # 8-5-4-3-A, gutshot
        self.assertFalse(is_gs([5, 4, 3], [14, 9]))  # 8-5-4-3-A, one card gutshot
        self.assertFalse(is_gs([5, 4, 3], [14, 14]))  # 9-5-4-3-A, paired gutshot
        self.assertFalse(is_gs([5, 4, 3], [14, 5]))  # A-5-5-4-3, paired gutshot
        self.assertFalse(is_gs([5, 4, 3], [14, 7]))  # A-7-5-4-3, double gutshot

    def test_double_gs(self):
        # Double gutshots
        self.assertFalse(is_gs([7, 5, 4], [14, 3]))  # 7-5-4-3-A, double gutshot
        self.assertFalse(is_gs([9, 6, 3], [7, 5]))  # 9-7-6-5-3, double gutshot
        
class TestIsOneCardGS(BaseTest):
    def test_oesd_gs(self):
        # Cases of OESD
        self.assertFalse(is_one_card_gs([10, 9, 8], [7, 5]))  # 10-9-8-7-5 forms a gutshot (6 needed)

    def test_complete_straight(self):
        # Cases where the board and hand already form a straight
        self.assertFalse(is_one_card_gs([10, 9, 8], [7, 6]))  # 10-9-8-7-6 forms a complete straight
        self.assertFalse(is_one_card_gs([14, 13, 12], [11, 10]))  # 14-13-12-11-10 forms a complete straight

    def test_one_card_gutshot(self):
        # Cases where no gutshot straight draw is present
        self.assertTrue(is_one_card_gs([10, 9, 7], [6, 5]))  # One card Gutshot
        self.assertTrue(is_one_card_gs([14, 13, 12], [10, 9]))  # One card Gutshot

    def test_paired_board(self):
        # Cases where the board is paired
        self.assertFalse(is_one_card_gs([9, 9, 8], [7, 5]))  # Paired flop 9-9-8 with gutshot
        self.assertFalse(is_one_card_gs([9, 8, 7], [8, 5]))  # Unpaired flop 10-10-9 with pair + gutshot

    def test_edge_cases(self):
        # Edge cases with Ace as high card
        self.assertFalse(is_one_card_gs([14, 12, 11], [10, 9]))  # A-Q-J-T-9, OESD
        self.assertTrue(is_one_card_gs([14, 13, 11], [10, 9]))  # A-K-J-T-9, one card gutshot

        # Edge case with Ace as low card
        self.assertFalse(is_one_card_gs([5, 4, 3], [14, 2]))  # 5-4-3-2-A, straight wheel
        self.assertFalse(is_one_card_gs([6, 5, 4], [14, 3]))  # 6-5-4-3-A, OESD
        self.assertFalse(is_one_card_gs([8, 5, 4], [14, 3]))  # 8-5-4-3-A, gutshot
        self.assertTrue(is_one_card_gs([5, 4, 3], [14, 9]))  # 9-5-4-3-A, one card gutshot
        self.assertFalse(is_one_card_gs([5, 4, 3], [14, 14]))  # 9-5-4-3-A, paired gutshot
        self.assertFalse(is_one_card_gs([5, 4, 3], [14, 5]))  # A-5-5-4-3, paired gutshot

    def test_double_gs(self):
        # Double gutshots
        self.assertFalse(is_one_card_gs([7, 5, 4], [14, 3]))  # 7-5-4-3-A, double gutshot
        self.assertFalse(is_one_card_gs([5, 4, 3], [14, 7]))  # A-7-5-4-3, double gutshot
        self.assertFalse(is_one_card_gs([9, 6, 3], [7, 5]))  # 9-7-6-5-3, double gutshot

class TestIsPairedGS(BaseTest):
    def test_oesd_gs(self):
        # Cases of OESD
        self.assertFalse(is_paired_gs([10, 9, 8, 7, 5], [10, 9, 8], [7, 5]))  # 10-9-8-7-5 forms a gutshot (6 needed)

    def test_complete_straight(self):
        # Cases where the board and hand already form a straight
        self.assertFalse(is_paired_gs([10, 9, 8, 7, 6], [10, 9, 8], [7, 6]))  # 10-9-8-7-6 forms a complete straight
        self.assertFalse(is_paired_gs([14, 13, 12, 11, 10], [14, 13, 12], [11, 10]))  # 14-13-12-11-10 forms a complete straight

    def test_one_card_gutshot(self):
        # Cases where no gutshot straight draw is present
        self.assertFalse(is_paired_gs([10, 9, 7, 6, 5], [10, 9, 7], [6, 5]))  # One card Gutshot
        self.assertFalse(is_paired_gs([14, 13, 12, 10, 9], [14, 13, 12], [10, 9]))  # One card Gutshot

    def test_paired_board(self):
        # Cases where the board is paired
        self.assertFalse(is_paired_gs([9, 9, 8, 7, 5], [9, 9, 8], [7, 5]))  # Paired flop 9-9-8 with gutshot
        self.assertTrue(is_paired_gs([9, 8, 8, 7, 5], [9, 8, 7], [8, 5]))  # Unpaired flop with pair + gutshot

    def test_edge_cases(self):
        # Edge cases with Ace as high card
        self.assertFalse(is_paired_gs([14, 12, 11, 10, 9], [14, 12, 11], [10, 9]))  # A-Q-J-T-9, OESD
        self.assertFalse(is_paired_gs([14, 13, 11, 10, 9], [14, 13, 11], [10, 9]))  # A-K-J-T-9, one card gutshot

        # Edge case with Ace as low card
        self.assertFalse(is_paired_gs([14, 5, 4, 3, 2], [5, 4, 3], [14, 2]))  # 5-4-3-2-A, straight wheel
        self.assertFalse(is_paired_gs([14, 6, 5, 4, 3], [6, 5, 4], [14, 3]))  # 6-5-4-3-A, OESD
        self.assertFalse(is_paired_gs([14, 8, 5, 4, 3], [8, 5, 4], [14, 3]))  # 8-5-4-3-A, gutshot
        self.assertFalse(is_paired_gs([14, 9, 5, 4, 3], [5, 4, 3], [14, 9]))  # 9-5-4-3-A, one card gutshot
        self.assertTrue(is_paired_gs([14, 14, 5, 4, 3], [5, 4, 3], [14, 14]))  # A-A-5-4-3, paired gutshot
        self.assertTrue(is_paired_gs([14, 5, 5, 4, 3], [5, 4, 3], [14, 5]))  # A-5-5-4-3, paired gutshot

    def test_double_gs(self):
        # Double gutshots
        self.assertFalse(is_paired_gs([14, 7, 5, 4, 3], [7, 5, 4], [14, 3]))  # 7-5-4-3-A, double gutshot
        self.assertFalse(is_paired_gs([9, 7, 6, 5, 3], [9, 6, 3], [7, 5]))  # 9-7-6-5-3, double gutshot


class TestIsDoubledGS(BaseTest):
    def test_oesd_gs(self):
        # Cases of OESD
        self.assertFalse(is_double_gs([10, 9, 8], [7, 5]))  # 10-9-8-7-5 forms a gutshot (6 needed)

    def test_complete_straight(self):
        # Cases where the board and hand already form a straight
        self.assertFalse(is_double_gs([10, 9, 8], [7, 6]))  # 10-9-8-7-6 forms a complete straight
        self.assertFalse(is_double_gs([14, 13, 12], [11, 10]))  # 14-13-12-11-10 forms a complete straight

    def test_one_card_gutshot(self):
        # Cases where no gutshot straight draw is present
        self.assertFalse(is_double_gs([10, 9, 7], [6, 5]))  # One card Gutshot
        self.assertFalse(is_double_gs([14, 13, 12], [10, 9]))  # One card Gutshot

    def test_paired_board(self):
        # Cases where the board is paired
        self.assertFalse(is_double_gs([9, 9, 8], [7, 5]))  # Paired flop 9-9-8 with gutshot
        self.assertFalse(is_double_gs([9, 8, 7], [8, 5]))  # Unpaired flop 10-10-9 with pair + gutshot

    def test_edge_cases(self):
        # Edge cases with Ace as high card
        self.assertFalse(is_double_gs([14, 12, 11], [10, 9]))  # A-Q-J-T-9, OESD
        self.assertFalse(is_double_gs([14, 13, 11], [10, 9]))  # A-K-J-T-9, one card gutshot

        # Edge case with Ace as low card
        self.assertFalse(is_double_gs([5, 4, 3], [14, 2]))  # 5-4-3-2-A, straight wheel
        self.assertFalse(is_double_gs([6, 5, 4], [14, 3]))  # 6-5-4-3-A, OESD
        self.assertFalse(is_double_gs([8, 5, 4], [14, 3]))  # 8-5-4-3-A, gutshot
        self.assertFalse(is_double_gs([5, 4, 3], [14, 9]))  # 9-5-4-3-A, one card gutshot
        self.assertFalse(is_double_gs([5, 4, 3], [14, 14]))  # 9-5-4-3-A, one card gutshot
        self.assertFalse(is_double_gs([5, 4, 3], [14, 5]))  # A-5-5-4-3, paired gutshot

    def test_double_gs(self):
        # Double gutshots
        self.assertTrue(is_double_gs([7, 5, 4], [14, 3]))  # 7-5-4-3-A, double gutshot
        self.assertTrue(is_double_gs([9, 6, 3], [7, 5]))  # 9-7-6-5-3, double gutshot


if __name__ == "__main__":
    unittest.main()
