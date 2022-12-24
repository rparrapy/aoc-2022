letter_to_shape = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
letter_to_outcome = {"X": 0, "Y": 3, "Z": 6}

shape_scores = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

outcome_to_shape = {
    "ROCK": {
        0: "SCISSORS",
        6: "PAPER" 
    },
    "PAPER": {
        0: "ROCK",
        6: "SCISSORS" 
    },
    "SCISSORS": {
        0: "PAPER",
        6: "ROCK" 
    }
}


def get_round_score(opp, me):
    outcome_score = letter_to_outcome[me]
    shape = letter_to_shape[opp] if outcome_score == 3 else outcome_to_shape[letter_to_shape[opp]][outcome_score]
    shape_score = shape_scores[shape]
    return outcome_score + shape_score

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return sum([get_round_score(*l.strip("\n").split(" ")) for l in lines])


if __name__ == "__main__":
    print(main())