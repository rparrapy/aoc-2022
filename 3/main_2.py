import functools
import string


def letter_to_priority(letter):
    return string.ascii_letters.index(letter) + 1

def group_to_priority(group):
    rucksacks = [set(r) for r in group]
    return sum(letter_to_priority(l) for l in functools.reduce(lambda a, b: a & b, rucksacks))


def groups(lines, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lines), n):
        yield lines[i:i + n]

def main():
    with open('input.txt') as f:
        lines = [l.strip("\n") for l in f.readlines()]
        return sum(group_to_priority(g) for g in groups(lines, 3))


if __name__ == "__main__":
    print(main())