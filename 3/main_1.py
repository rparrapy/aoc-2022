import string


def letter_to_priority(letter):
    return string.ascii_letters.index(letter) + 1

def rucksack_to_priority(rucksack):
    half = int(len(rucksack) / 2)
    comp_1 = set(rucksack[:half])
    comp_2 = set(rucksack[half:])
    return sum(letter_to_priority(l) for l in comp_1 & comp_2)

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return sum(rucksack_to_priority(r.strip("\n")) for r in lines)


if __name__ == "__main__":
    print(main())