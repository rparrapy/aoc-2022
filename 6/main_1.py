MARKER_LENGTH = 4

def first_marker_pos(buffer):
    for i in range(len(buffer) - (MARKER_LENGTH - 1)):
        sub_buffer = buffer[i:i+MARKER_LENGTH]
        if len(set(sub_buffer)) == MARKER_LENGTH:
            return i + MARKER_LENGTH

def main():
    with open('input.txt') as f:
        line = f.readlines()[0]
        return first_marker_pos(line)

if __name__ == "__main__":
    print(main())