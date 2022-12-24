def get_calories_by_elf():
    with open('input.txt') as f:
        lines = f.readlines()
        result = []
        acc = 0
        for l in lines:
            if l == "\n":
                result.append(acc)
                acc = 0
            else:
                acc += int(l)
        return result


def main():
    calories_counts = get_calories_by_elf()
    return sum(sorted(calories_counts, reverse=True)[:3])


if __name__ == "__main__":
    print(main())