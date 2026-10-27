import random
import typing


def gen_event(
        players: list[str], actions: list[str]
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event: tuple[str, str] = random.choice(event_list)
        event_list.remove(event)
        yield event


def show_event(event: tuple[str, str], index: int = -1) -> None:
    if index >= 0:
        print(f"Event {index}: ", end="")
    print(
        f"Player {event[0]} "
        "did action "
        f"{event[1]}"
    )


def generate_events(
    amount: int,
    event_generator: typing.Generator[tuple[str, str], None, None],
    is_show: bool = False
) -> list[tuple[str, str]]:
    event_list: list[tuple[str, str]] = []
    for i in range(0, amount):
        event: tuple[str, str] = next(event_generator)
        event_list.append(event)
        if is_show:
            show_event(event, i)
    return event_list


def delete_events(
    event_list: list[tuple[str, str]],
    event_generator: typing.Generator[tuple[str, str], None, None],
    is_show: bool = False
) -> list[tuple[str, str]]:
    for event in event_generator:
        if is_show:
            print(f"Got event from list: {event}")
            print(f"Remains in list: {event_list}")
    return event_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    all_players: list[str] = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N"
    ]
    all_actions: list[str] = [
        "run",
        "dance",
        "swim",
        "bluff",
        "walk",
        "hit",
        "die",
        "heal",
        "speak",
        "shout",
        "cook",
        "freeze",
        "try"
    ]
    event_generator: typing.Generator[
        tuple[str, str], None, None
    ] = gen_event(all_players, all_actions)

    generate_events(1000, event_generator, True)

    event_list: list[tuple[str, str]] = generate_events(10, event_generator)
    print(f"Built list of 10 events: {event_list}")

    event_consumer: typing.Generator[
        tuple[str, str], None, None
    ] = consume_event(event_list)

    event_list = delete_events(event_list, event_consumer, True)
