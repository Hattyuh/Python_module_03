import sys


class Scoreboard():
    def __init__(self) -> None:
        self.edge_size: int = 5
        self.inner_size: int = 35


def print_scoreboard_edge(sc: Scoreboard) -> None:
    print(
        f"{'':*<{sc.edge_size * 2 + sc.inner_size}}\n"
        f"{'':*<{sc.edge_size * 2 + sc.inner_size}}"
    )


def print_row(
        sc: Scoreboard,
        text: str = "",
        score: int = 0,
        is_score: bool = False
) -> None:
    if is_score:
        print(
            f"{'***':<{sc.edge_size}}"
            f"{f'{score}':<{sc.inner_size}}"
            f"{'***':>{sc.edge_size}}"
        )
    else:
        print(
            f"{'***':<{sc.edge_size}}"
            f"{f'{text}':<{sc.inner_size}}"
            f"{'***':>{sc.edge_size}}"
        )


def show_scoreboard(sc: Scoreboard, scores: list[int]) -> None:
    print()
    print_scoreboard_edge(sc)
    print_row(sc, "")
    print_row(sc, "Scores processed:")
    for score in scores:
        print_row(sc, score=score, is_score=True)
    print_row(sc, "")
    print_row(sc, "Total players:")
    print_row(sc, score=len(scores), is_score=True)
    print_row(sc, "")
    print_row(sc, "Total score:")
    print_row(sc, score=sum(scores), is_score=True)
    print_row(sc, "")
    print_row(sc, "Avarage score:")
    print_row(sc, score=int(sum(scores) / len(scores)), is_score=True)
    print_row(sc, "")
    print_row(sc, "High score:")
    print_row(sc, score=max(scores), is_score=True)
    print_row(sc, "")
    print_row(sc, "Low score:")
    print_row(sc, score=min(scores), is_score=True)
    print_row(sc, "")
    print_row(sc, "Score range:")
    print_row(sc, score=max(scores) - min(scores), is_score=True)
    print_row(sc, "")
    print_scoreboard_edge(sc)
    print()


def get_score(score: str) -> int:
    return int(score)


def validate_list(
        list_to_validate: list[int] | list[str],
        valid_len: int
) -> None:
    if len(list_to_validate) < valid_len:
        raise ValueError(
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )


def main() -> None:
    try:
        validate_list(sys.argv, 2)
    except ValueError as error:
        print(f"No scores provided. Usage: {error}")
        return
    scores: list[int] = []
    for score in sys.argv[1:]:
        try:
            scores.append(get_score(score))
        except ValueError:
            print(f"Invalid parameter '{score}'")
    try:
        validate_list(scores, 1)
    except ValueError as error:
        print(f"No scores provided. Usage: {error}")
        return
    sc = Scoreboard()
    show_scoreboard(sc, scores)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
