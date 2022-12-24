def range_to_sections(r):
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    return set(range(start, end + 1))


def fully_contains(a, b):
    sections_a = range_to_sections(a)
    sections_b = range_to_sections(b)
    return not (sections_a - sections_b) or not (sections_b - sections_a)

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return sum(fully_contains(*l.strip("\n").split(",")) for l in lines)


if __name__ == "__main__":
    print(main())