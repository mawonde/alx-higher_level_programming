#!/usr/bin/python3
""" Module for printing status codes. """
import sys


class Magic:
    """ Class for generating instances with a dictionary and size."""
    def __init__(self):
        """Initialize a Magic instance."""
        self.dic = {}
        self.size = 0

    def init_dic(self):
        """ Initialize the dictionary with status codes."""
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_status_code(self, status):
        """ Add to the count of a specific status code. """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        """ Print the status codes and file size."""
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] is not 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines is not 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()
