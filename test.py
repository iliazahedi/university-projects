import random

RED, BLUE, DIM, BOLD, RESET = "\033[91m", "\033[94m", "\033[2m", "\033[1m", "\033[0m"

MAX_MARKS = 3
MAX_TURNS = 40

LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def other(p):
    return "O" if p == "X" else "X"


def cell_str(board, marks, i):
    p = board[i]

    if p == " ":
        return f"{DIM}{i + 1}{RESET}"

    color = RED if p == "X" else BLUE

    fading = len(marks[p]) == MAX_MARKS and marks[p][0] == i

    return (
        f"{DIM}{color}{p}{RESET}"
        if fading
        else f"{BOLD}{color}{p}{RESET}"
    )


def print_board(board, marks):
    print()

    for r in range(3):
        print(
            " " + " | ".join(
                cell_str(board, marks, r * 3 + c)
                for c in range(3)
            )
        )

        if r < 2:
            print("---+---+---")

    print(f"{DIM}(dim mark = vanishes on your next move){RESET}\n")


def winner(board):
    for a, b, c in LINES:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def free_cells(board):
    return [i for i in range(9) if board[i] == " "]


def place(board, marks, p, idx):
    """Return a NEW board/marks after player p plays idx."""

    board = board[:]

    marks = {
        k: v[:]
        for k, v in marks.items()
    }

    if len(marks[p]) == MAX_MARKS:
        old = marks[p].pop(0)
        board[old] = " "

    board[idx] = p
    marks[p].append(idx)

    return board, marks


def minimax(board, marks, turn, ai, depth):
    w = winner(board)

    if w == ai:
        return 100 + depth

    if w:
        return -100 - depth

    if depth == 0:
        return 0

    scores = [
        minimax(
            *place(board, marks, turn, i),
            other(turn),
            ai,
            depth - 1
        )
        for i in free_cells(board)
    ]

    return max(scores) if turn == ai else min(scores)


def ai_move(board, marks, ai, level):
    cells = free_cells(board)

    if level == "1":
        return random.choice(cells)

    depth = 2 if level == "2" else 5

    scores = {
        i: minimax(
            *place(board, marks, ai, i),
            other(ai),
            ai,
            depth
        )
        for i in cells
    }

    best = max(scores.values())

    return random.choice([
        i for i, s in scores.items()
        if s == best
    ])


def human_move(board, player):
    while True:
        choice = input(
            f"Player {player}, pick a cell (1-9): "
        ).strip()

        if (
            choice.isdigit()
            and 1 <= int(choice) <= 9
            and board[int(choice) - 1] == " "
        ):
            return int(choice) - 1

        print("Invalid move, try again.")


def play_round(mode, level):
    board = [" "] * 9
    marks = {
        "X": [],
        "O": []
    }

    current = "X"

    for _ in range(MAX_TURNS):

        print_board(board, marks)

        if mode == "2" and current == "O":
            idx = ai_move(
                board,
                marks,
                "O",
                level
            )

            print(f"Computer plays cell {idx + 1}")

        else:
            idx = human_move(
                board,
                current
            )

        board, marks = place(
            board,
            marks,
            current,
            idx
        )

        if winner(board):
            print_board(board, marks)

            print(
                f"{BOLD}{current} wins! 🎉{RESET}"
            )

            return current

        current = other(current)

    print("Turn limit reached, it's a draw!")

    return "draw"


def main():
    print(
        f"{BOLD}=== Vanishing Tic-Tac-Toe 👻 ==={RESET}"
    )

    print(
        f"{BOLD}Rule: you can only have {MAX_MARKS} marks. "
        f"Placing a new one removes your oldest!{RESET}\n"
    )

    mode = input(
        "1) Two players   2) vs computer : "
    ).strip()

    level = "3"

    if mode == "2":
        level = input(
            "Difficulty: 1) Easy  2) Medium  3) Hard : "
        ).strip() or "3"

    score = {
        "X": 0,
        "O": 0,
        "draw": 0
    }

    while True:

        result = play_round(
            mode,
            level
        )

        score[result] += 1

        print(
            f"\nScore -> "
            f"{RED}X: {score['X']}{RESET} | "
            f"{BLUE}O: {score['O']}{RESET} | "
            f"Draws: {score['draw']}"
        )

        if input(
            "Play again? (y/n): "
        ).strip().lower() != "y":

            print("Thanks for playing!")

            break


if __name__ == "__main__":
    main()