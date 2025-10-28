inventory = {
    "SKU001": {"product_name": "Apples", "quantity": 30},
    "SKU002": {"product_name": "Bananas", "quantity": 45},
    "SKU003": {"product_name": "Oranges", "quantity": 0},
    "SKU004": {"product_name": "Tomatoes", "quantity": 3},
    "SKU005": {"product_name": "Pears", "quantity": 5}
}

skus = inventory.keys()

for sku in skus:
    if inventory[sku]['quantity'] < 10:
        print(f"Reorder {inventory[sku]['product_name']}({sku}). Low inventory ({inventory[sku]['quantity']}).")
    else:
        print(f"Plenty of {inventory[sku]['product_name']}. No need to reorder yet.")