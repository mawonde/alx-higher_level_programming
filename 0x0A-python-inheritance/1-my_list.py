#!/usr/bin/python3
class MyList(list):
    """A class that inherits the attributes and methods of the built-in list class.

    Args:
        list: The built-in list class.

    """

    def print_sorted(self):
        """Prints the sorted list.

        This method creates a copy of the list, sorts it in ascending order, and then prints it.
        """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)

