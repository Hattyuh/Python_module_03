import math


def get_player_pos() -> tuple[float, float, float]:
    is_valid: bool = False
    while not is_valid:
        values: list[str] = input(
            "Enter new coordinates as floats in format 'x,y,z':"
        ).split(",")
        if len(values) != 3:
            print("Invalid syntax")
        else:
            try:
                numbers: list[float] = []
                for value in values:
                    numbers.append(float(value))
                is_valid = True
            except ValueError as error:
                print(f"Error on parameter '{value}': {error}")
    coordinates: tuple[float, float, float] = (
        float(values[0]), float(values[1]), float(values[2])
    )
    return coordinates


def calculate_distance(
        point1: tuple[float, float, float],
        point2: tuple[float, float, float] = (0, 0, 0)
) -> float:
    return math.sqrt(
        (point2[0] - point1[0])**2 +
        (point2[1] - point1[1])**2 +
        (point2[2] - point1[2])**2
    )


def ft_coordinate_system() -> None:
    first_coordinates: tuple[float, float, float] = get_player_pos()
    print("Get a first set of coordinates")
    print(f"Got a first tuple: {first_coordinates}")
    print(
        "It includes: "
        f"X={first_coordinates[0]}, "
        f"Y={first_coordinates[1]}, "
        f"Z={first_coordinates[2]}"
    )
    print(f"Distance to center: {calculate_distance(first_coordinates):.4f}")
    print()
    print("Get a second set of coordinates")
    second_coordinates: tuple[float, float, float] = get_player_pos()
    print("Distance between two set of coordinates: "
          f"{calculate_distance(first_coordinates, second_coordinates):.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()
