from collections import Counter
from itertools import combinations

if __name__ == "__main__":
    f = open('input.txt').read().splitlines()

    # Part I
    a = sum(int(2 in Counter(i).values()) for i in f)
    b = sum(int(3 in Counter(i).values()) for i in f)
    print(f"1st Part: {a*b}")

    # Part II
    def hamming_distance(u: str, v: str) -> int:
        return sum(int(i != j) for i, j in zip(u, v))

    for u, v in combinations(f, 2):
        if hamming_distance(u, v) == 1:
            print(f"2nd Part: {''.join(i for i, j in zip(u, v) if i == j)}")
# Part I could be improved to avoid running through the list 2 times
