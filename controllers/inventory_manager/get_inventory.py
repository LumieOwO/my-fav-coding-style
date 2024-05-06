from typing import Dict, Any, List


def get_inventory(self) -> List[Dict[str, Any]]:
    """
    Retrieve the current inventory.

    Returns:
        list: A list of dictionaries representing the inventory.
    """
    return self.inventory
