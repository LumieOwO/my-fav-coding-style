from controllers.inventory_manager.main import InventoryManager
import utilities
import utilities.constants


def main() -> None:
    inventory_manager = InventoryManager(utilities.constants)
    inventory_manager.add_product(["uwu"])
    print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
