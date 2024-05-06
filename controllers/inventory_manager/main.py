from controllers.inventory_manager.add_product import add_product
from controllers.inventory_manager.get_inventory import get_inventory
from typing import Dict, Any, Tuple, List


class InventoryManager:
    def __init__(self, constants):
        self.inventory = []
        self.constants = constants

    def add_product(
        self, product_data: Dict[str, Any] | str
    ) -> Tuple[str, Dict[str, Any]]:
        try:
            result = add_product(self=self, product_data="uwu")
            return result
        except Exception as e:
            return (self.constants.FAILURE, str(e))

    def get_inventory(self) -> List[Dict[str, Any]]:
        return get_inventory(self=self)
