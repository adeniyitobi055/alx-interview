#!/usr.bin/python3
"""
0-lockedboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if not unlocked[key]:
            unlocked[key] = True
            new_keys = boxes[key]
            keys.extend(new_keys)

    return all(unlocked)
