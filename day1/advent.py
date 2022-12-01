with open('input.txt', 'r') as f:
    inventories = [[int(n) for n in inventory.split('\n')] for inventory in f.read().split('\n\n')]
    inventory_calories = sorted([sum(inventory) for inventory in inventories], reverse=True)

answer1 = inventory_calories[0]
answer2 = sum(inventory_calories[:3])
print(answer1, answer2)