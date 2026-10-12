def get_player_pos() -> tuple[float, float, float]:

    while True:
        values: list[str] = input("Enter new coordinates as floats in format 'x,y,z':").split(",")
        if len(values) == 3:
            try:
                for value in values:
                    float(value)
            except:
                print("Invalid syntax")        
        else:
            print("Invalid syntax")
            
    coordinates: tuple[float, float, float]
    return coordinates

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print(get_player_pos())