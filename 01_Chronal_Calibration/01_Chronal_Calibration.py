from collections import defaultdict

if __name__ == "__main__":
    def main():
        f = open('input.txt').read().splitlines()

        # Part I
        int_list = list(map(int, f))
        print(f"1st Part: {sum(int_list)}")

        # Part II
        dd = defaultdict(int)
        i = 0

        while True:
            for number in int_list:
                dd[i] += 1
                if dd[i] == 2:
                    print(f"2nd Part: {i}")
                    return 1
                i += number

    main()
