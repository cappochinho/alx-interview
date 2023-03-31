"""
Contains canUnlockAll() method that determines
if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    # Create a list of booleans to keep track of which boxes can be unlocked

    can_unlock = [False] * len(boxes)
    can_unlock[0] = True

    keys_to_try = boxes[0]

    while len(keys_to_try) > 0:
        for key in keys_to_try:
            if key < len(boxes) and not can_unlock[key]:
                can_unlock[key] = True
                keys_to_try += boxes[key]

        keys_to_try = list(set(keys_to_try) - set(range(len(boxes))))

    return all(can_unlock)
