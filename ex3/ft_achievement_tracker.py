import random


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements: set[str] = gen_player_achievements(all_achievements)
        self.show()

    def show(self) -> None:
        print(
            f"Player {self.name}: "
            f"{self.achievements}"
        )


def gen_player_achievements(achievements: list[str]) -> set[str]:
    achievement_count: int = random.randint(1, len(achievements))
    return set(random.sample(achievements, k=achievement_count))


def create_data(
        mode: str,
        players: list[Player],
        all_achievements: list[str],
        main_player: int = 0
) -> set[str]:
    data: list[set[str]] = []
    if mode == "missing":
        data.append(set(all_achievements))
        data.append(players[main_player].achievements)
        return set.difference(*data)
    data.append(players[main_player].achievements)
    for index, player in enumerate(players):
        if index != main_player:
            data.append(player.achievements)
    if mode == "distinct":
        return set.union(*data)
    elif mode == "common":
        return set.intersection(*data)
    elif mode == "only":
        return set.difference(*data)
    else:
        raise ValueError(f"Invalid mode: {mode}")


if __name__ == "__main__":
    print("== Achievement tracker system ==\n")
    all_achievements: list[str] = [
        "1 Duck catcher",
        "2 Hobbit finder",
        "3 Soul eater",
        "4 Lucky chuck",
        "5 Family friendly",
        "6 Famous musician",
        "7 Curious granny"
    ]
    all_players: list[Player] = [
        Player("Anna"),
        Player("Bob"),
        Player("Charlie"),
        Player("david")
    ]
    print()
    print(
        "All distinct achievements: "
        f"{create_data("distinct", all_players, all_achievements)}"
    )
    print()
    print(
        "Common achievements: "
        f"{create_data("common", all_players, all_achievements)}"
    )
    print()
    for index, player in enumerate(all_players):
        print(
            f"Only {player.name} has: "
            f"{create_data("only", all_players, all_achievements, index)}"
        )
    print()
    for index, player in enumerate(all_players):
        print(
            f"{player.name} is missing: "
            f"{create_data("missing", all_players, all_achievements, index)}"
        )
