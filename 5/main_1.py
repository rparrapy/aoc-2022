import re


def parse_crate_line(line):
    return [line[i] for i in range(1, len(line), 4)]

def process_move(stacks, number_of_crates, from_stack, to_stack):
    for _ in range(number_of_crates):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return stacks


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        crate_rows = []
        stacks = []
        for line in lines:
            if line.strip(" ").startswith("["):
                crate_rows.append(parse_crate_line(line))
            elif line.strip(" ").startswith("move"):
                number_of_crates, from_stack, to_stack = re.findall(r'\d+', line)
                stacks = process_move(stacks, int(number_of_crates), int(from_stack) - 1, int(to_stack) - 1)
            else:
                stacks = [[e for e in list(cr) if e != " "] for cr in zip(*reversed(crate_rows))]
        print(stacks)
        return "".join([s[-1] for s in stacks])

if __name__ == "__main__":
    print(main())