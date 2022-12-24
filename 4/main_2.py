def range_to_sections(r):
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    return set(range(start, end + 1))


def overlaps(a, b):
    sections_a = range_to_sections(a)
    sections_b = range_to_sections(b)
    return bool(sections_a & sections_b)

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return sum(overlaps(*l.strip("\n").split(",")) for l in lines)


if __name__ == "__main__":
    print(main())