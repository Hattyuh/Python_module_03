import sys


def showf_args() -> None:
    arg_count = len(sys.argv)
    i: int = 0
    for arg in sys.argv:
        if i == 0:
            print(f"Program name: {arg}")
            if arg_count < 2:
                print("No arguments provided!")
            else:
                print(f"Arguments recieved: {arg_count - 1}")
        else:
            print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {arg_count}")
    print()


if __name__ == "__main__":
    print("=== Command Quest ===")
    showf_args()
