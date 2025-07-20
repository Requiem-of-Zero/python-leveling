character_inventory = {
  'rope': 1,
  'torch' : 6,
  'gold coin': 42,
  'dagger': 1,
  'arrow': 12
}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
  total = 0
  print("Inventory: ")
  for item, quantity in inventory.items():
    total += quantity
    print(quantity, item)
  print(f"Total items in inventory: {total}")

def add_to_inventory(inventory, added_items):
  for item in added_items:
    inventory[item] = inventory.get(item, 0) + 1

add_to_inventory(character_inventory, dragon_loot)
display_inventory(character_inventory)