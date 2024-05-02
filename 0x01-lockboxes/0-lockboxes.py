#!/usr/bin/python3

""" canUnloackAll function """


def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened.
    """

    # number of boxes
    n = len(boxes)
    # all boxes are locked except the 1st
    opened_boxes = [False]*n  # false times num of boxes
    opened_boxes[0] = True
    keys = [key for key in boxes[0]]

    # pop a key from stack if there are keys
    while keys:
        key = keys.pop()
    # if a key corresponse to a box it is opened
        if key < n and not opened_boxes[key]:
            opened_boxes[key] = True
            keys.extend(boxes[key])  # extend the list

    return all(opened_boxes)
