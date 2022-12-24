letter_to_shape = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS", "X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}

shape_scores = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

outcome_scores = {
    "ROCK": {
        "PAPER": 0,
        "SCISSORS": 6 
    },
    "PAPER": {
        "ROCK": 6,
        "SCISSORS": 0
    },
    "SCISSORS": {
        "ROCK": 0,
        "PAPER": 6
    }
}

def get_round_score(opp, me):
    outcome_score = 3 if letter_to_shape[me] == letter_to_shape[opp] else outcome_scores[letter_to_shape[me]][letter_to_shape[opp]]
    shape_score = shape_scores[letter_to_shape[me]]
    return outcome_score + shape_score

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return sum([get_round_score(*l.strip("\n").split(" ")) for l in lines])


if __name__ == "__main__":
    print(main())