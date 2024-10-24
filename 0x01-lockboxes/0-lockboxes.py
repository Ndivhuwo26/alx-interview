#!/usr/bin/python3

def canUnlockAll(boxes):
    """Check if all boxes can be opened."""
    if len(boxes) == 0:
        return False

    """ A set to track which boxes have been opened"""
    opened = {0}
    keys = boxes[0]

    """ Iterate over the available keys"""
    for key in keys:
        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
