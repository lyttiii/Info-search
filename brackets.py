BRACKET_PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
}
OPENING = set(BRACKET_PAIRS.values())
CLOSING = set(BRACKET_PAIRS.keys())


def read_brackets_from_console(prompt: str = "Введите скобочную последовательность: ") -> str:
    return input(prompt).strip()


def extract_brackets(s: str) -> str:
    allowed = OPENING.union(CLOSING)
    return "".join(ch for ch in s if ch in allowed)


def check_bracket_sequence(seq: str) -> bool:
    stack = []  

    for ch in seq:
        if ch in OPENING:
            stack.append(ch)
        elif ch in CLOSING:
            if not stack:
                return False
            last_open = stack.pop()
            if last_open != BRACKET_PAIRS[ch]:
                return False

    return not stack 


def main() -> None:
    user_input = read_brackets_from_console()
    bracket_seq = extract_brackets(user_input)

    if bracket_seq != user_input and bracket_seq != "":
        print(f"Используемая последовательность: {bracket_seq}")

    is_correct = check_bracket_sequence(bracket_seq)

    if is_correct:
        print("Правильная скобочная последовательность")
    else:
        print("Неправильная скобочная последовательность")


if __name__ == "__main__":
    main()
