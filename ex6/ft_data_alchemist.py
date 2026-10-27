import random


if __name__ == "__main__":
    player_names: list[str] = [
        "Anna", "bob", "Joe", "Lue", "sarah", "victor"
    ]
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {player_names}")
    all_cap_players: list[str] = [name.capitalize() for name in player_names]
    print(f"New list with all names capitalized: {all_cap_players}")
    only_cap_players: list[str] = [
        name for name in player_names if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_cap_players}")
    print()
    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_cap_players
    }
    print(f"Score dict: {score_dict}")
    score_avarage: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score avarage is {score_avarage}")
    highscore_dict: dict[str, int] = {
        name: score for name,
        score in score_dict.items() if score > score_avarage
    }
    print(f"High scores: {highscore_dict}")
