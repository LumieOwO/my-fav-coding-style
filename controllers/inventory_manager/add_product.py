from typing import Dict, Any, Tuple


def add_product(self, product_data: Dict[str, Any] | str) -> Tuple[str, Dict[str, Any]]:
    """
    Add a new product to the inventory.

    Args:
        product_data (dict): A dictionary containing product information.
            Example: {'name': 'Apple', 'price': 1.99, 'quantity': 100}

    Returns:
       array:[ dict: A message indicating success or failure,str: the updated data.]
    """
    self.inventory.append(product_data)
    return {"message": f"{product_data['name']} added to inventory successfully."}
