from collections import defaultdict

# lines = [l.strip().split() for l in open("AOC2023/aoc07/test_input.txt").readlines()]
lines = [l.strip().split() for l in open("AOC2023/aoc07/input.txt").readlines()]


number_deck = len(lines)

ord_values = {
    "A": "e",
    "K": "d",
    "Q": "c",
    "J": "1",  # "b",
    "T": "a",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2",
}


class Hand:
    def __init__(self, hand, bid):
        self._cards = []
        self.bid = int(bid)
        self.hand = hand
        self.counts = defaultdict(int)
        self.s_hand = "".join(ord_values[h] for h in hand)
        self.rank = -1

        self.analyze(hand)

    def find_num(self, num):
        for c in self.counts:
            if self.counts[c] == num:
                return c
        return None

    def analyze(self, hand):
        for h in hand:
            self.counts[h] += 1

        # print(f"new {hand=} {self.bid=}")
        sz_type = len(self.counts)
        if sz_type == 1:
            self.type = 1  # "FIVE_KIND"
        elif sz_type == 2:
            if self.find_num(4) is not None:
                self.type = 2  # "FOUR_KIND"
            elif self.find_num(3) is not None:
                self.type = 3  # FULL house
        elif sz_type == 3:
            if self.find_num(3) is not None:
                self.type = 4  # Three of kind
            elif self.find_num(2) is not None:
                self.type = 5  # two pairs
        elif sz_type == 4:
            if self.find_num(2) is not None:
                self.type = 6  # one pair
        elif sz_type == 5:
            self.type = 7  # High card

    def adjust(self):
        if "J" in self.hand:
            if self.type == 2:  # "FOUR_KIND"
                self.type = 1  # "FIVE_KIND"
            elif self.type == 3:  # FULL house
                self.type = 1  # "FIVE_KIND"
            elif self.type == 4:  # Three of kind
                self.type = 2  # "FOUR_KIND"
            elif self.type == 5:  # two pairs
                if self.counts["J"] == 1:
                    self.type = 3  # FULL house
                else:
                    self.type = 2  # "FOUR_KIND"
            elif self.type == 6:  # one pair
                self.type = 4  # Three of kind
            elif self.type == 7:  # High card
                self.type = 6  # one pair

    def print_rank(self):
        dd = {
            1: "FIVE KIND",
            2: "FOUR KIND",
            3: "FULL-HOUSE KIND",
            4: "THREE KIND",
            5: "TWO PAIRS KIND",
            6: "ONE PAIR KIND",
            7: "HIGHT CARD KIND",
        }

        print(f"{self.hand=} rank={dd[self.type]}")


hands = defaultdict(list)

rank = number_deck

for l in lines:
    hand = Hand(l[0], l[1])
    hand.adjust()
    if "J" in hand.hand:
        hand.print_rank()
    hands[hand.type].append(hand)

for kind_type in range(1, 8):
    if len(hands[kind_type]) > 0:
        _h = sorted(
            range(len(hands[kind_type])), key=lambda k: hands[kind_type][k].s_hand
        )[::-1]
        for a in _h:
            hands[kind_type][a].rank = rank
            rank -= 1


sum_bid = 0
for h in hands:
    for hand in hands[h]:
        sum_bid += hand.rank * hand.bid


print(sum_bid)
