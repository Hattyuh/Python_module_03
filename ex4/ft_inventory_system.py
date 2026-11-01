import sys


class Inventory:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def show_dict(self) -> None:
        print(self.items)

    def show_item_list(self) -> None:
        print(f"Item list: {list(self.items.keys())}")

    def show_item_quantity(self) -> None:
        print(
            f"Total quantity of the {len(self.items.values())} "
            f"items: {sum(self.items.values())}"
        )

    def show_percantages(self) -> None:
        for item in self.items.keys():
            print(
                f"Item {item} represents "
                f"{round(
                    self.items[item] / sum(self.items.values()) * 100, 1
                )}%"
            )

    def show_most_abdunant_item(self) -> None:
        try:
            max_value: int = list(self.items.values())[0]
            most_abundant_item: str = list(self.items.keys())[0]
        except IndexError:
            print(
                "Error - empty dictionary: "
                "most abdunant item can't be found"
            )
            return
        for item in self.items.keys():
            if self.items[item] > max_value:
                max_value = self.items[item]
                most_abundant_item = item
        print(
            f"Item most abundant: {most_abundant_item} "
            f"with quantity {self.items[most_abundant_item]}"
        )

    def show_least_abdunant_item(self) -> None:
        try:
            min_value: int = list(self.items.values())[0]
            least_abundant_item: str = list(self.items.keys())[0]
        except IndexError:
            print(
                "Error - empty dictionary: "
                "least abdunant item can't be found"
            )
            return
        for item in self.items.keys():
            if self.items[item] < min_value:
                min_value = self.items[item]
                least_abundant_item = item
        print(
            f"Item least abundant: {least_abundant_item} "
            f"with quantity {self.items[least_abundant_item]}"
        )

    def add_item(self, item_name: str, quantity: int) -> None:
        if item_name in self.items:
            print(f"Redundant item '{item_name}' - discarding")
        elif not item_name:
            print("Item name can't be empty - discarding")
        else:
            if quantity <= 0:
                raise ValueError("Should be grater than zero")
            self.items.update({item_name: quantity})


def parse_input(args: list[str]) -> Inventory:
    my_inventory = Inventory()
    for i in range(len(args)):
        if i > 0:
            item: list[str] = args[i].split(":")
            try:
                if len(item) != 2:
                    raise IndexError
                my_inventory.add_item(item[0], int(item[1]))
            except ValueError as error:
                print(f"Quantity error for '{item[0]}': {error}")
            except IndexError:
                print(f"Error - invalid parameter '{item[0]}'")
    return my_inventory


def test_inventory(i: Inventory) -> None:
    i.show_dict()
    i.show_item_list()
    i.show_item_quantity()
    i.show_percantages()
    i.show_most_abdunant_item()
    i.show_least_abdunant_item()


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    empty_inventory = Inventory()
    print("Empty Inventory Check ->")
    test_inventory(empty_inventory)
    print()
    print("Parsing input ->")
    my_inventory: Inventory = parse_input(sys.argv)
    print()
    print("Inventory Check ->")
    print("Got inventory: ", end="")
    test_inventory(my_inventory)
    print()
    print("Updating inventory ->")
    my_inventory.add_item("sword", 2)
    my_inventory.add_item("ham", 3)
    print()
    print("Updated inventory: ", end="")
    my_inventory.show_dict()
