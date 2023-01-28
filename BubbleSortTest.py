# Name: Karston Hunt
# GitHub: Karstonhunt
# Date: 1/27/2023
# Description: Function sorts list of boxes based on volume of each box in that list.

class Box:
    """Represents a box with length, width, and height."""

    def __init__(self, length, width, height):
        """Initializes private length, width, and height for box object."""
        self._length = length
        self._width = width
        self._height = height

    def box_volume(self):
        """Returns volume of box class object."""
        volume = self._length * self._width * self._height
        return volume

    def get_length(self):
        """Returns box length."""
        return self._length

    def get_width(self):
        """Returns box width"""
        return self._width

    def get_height(self):
        """Returns box height"""
        return self._height


def box_sort(box_list):
    """"""
    list_length = len(box_list)
    original_list_volumes = []

    for i in box_list:
        volume = i.box_volume()
        original_list_volumes.append(volume)

    for num in range(list_length - 1):
        for box in range(list_length - 1):
            if box_list[box].box_volume() > box_list[box + 1].box_volume():
                temp_box = box_list[box]
                box_list[box] = box_list[box + 1]
                box_list[box + 1] = temp_box
            else:
                box_list[box] = box_list[box]

    for i in range(len(box_list)):
        volume = box_list[i].box_volume()
        box_list[i] = volume

    print(f"Original list volumes: {original_list_volumes} \nOrdered list: {box_list}")


b1 = Box(3.4, 19.8, 2.1)
b2 = Box(8.2, 8.2, 4.5)
b3 = Box(1.0, 1.0, 1.0)
b4 = Box(3.9, 8.0, 7)
b5 = Box(1, 12, 5)
b6 = Box(8, 1.9, 1.2)
b7 = Box(4, 15.8, 1)
b8 = Box(9.2, 9.2, 7.5)
b9 = Box(1.0, 1.0, 1.0)
list_of_boxes = [b1, b2, b3]
box_sort(list_of_boxes)
