class Box:
    """Class defines a box and has functions to compute: volume, surface area,
    and Girth+depth mesurements.


    Method signatures:
    Box.__init__(self, l:float, w:float, d:float):
    Box.findVolume(self, l, w, d): -> float
    Box.findArea(self, l, w, d): -> float
    Box.findGirthDepth(self, l, w, d): -> float

    Note: all l, w, d can be assumed to be length, width, and depth respectively.
    """

    def __init__(self, l: float = None, w: float = None, d: float = None):
        # gate keeping to make sure that we actually have values
        if None in [l, w, d]:
            raise Exception("please specify lenth, width, and depth of box")

        self.V = self.findVolume(l, w, d)
        self.A = self.findArea(l, w, d)
        self.GD = self.findGirthDepth(l, w, d)

    def findVolume(self, l, w, d):
        """returns lwd"""
        return l * w * d

    def findArea(self, l, w, d):
        """returns 2lw + 2wd + 2ld"""
        return (2 * (l * w)) + (2 * (w * d)) + (2 * (l * d))

    def findGirthDepth(self, l, w, d):
        """returns 2lw + d"""
        return (2 * (l + w)) + d

    def __repr__(self) -> str:
        # change string repersent method to make exspected ouput
        # print when object is passed to print built-in
        return (
            f"Volume = {self.V:.1f}\n"
            + f"Area = {self.A:.1f}\n"
            + f"Girth and Depth = {self.GD:.1f}"
        )


if __name__ == "__main__":
    while True:
        # store input from user
        p = input()

        # check break condition first and quit if condition is true
        if p.lower()[0] == "q":
            break

        # check edge case where not using 'C' as the command letter
        if p[0] != "C":
            print("please enter 3 numbers following the command character")
            print("Examples: 'C 1 2 3','C 1.7 2.2 3.2', 'C 1 2.2 15'")
            break

        # remove command character from input then strip leading lagging
        # whitespace then split into inputs for functions
        p = p[1:].strip().split()

        # check number of inputs before continuing, quit if can't unpack
        if len(p) != 3:
            print("please enter 3 numbers following the command character")
            print("Examples: 'C 1 2 3','C 1.7 2.2 3.2', 'C 1 2.2 15'")
            break

        # un-pack input values into their respective variables
        l, w, d = p

        # cast to float
        l, w, d = float(l), float(w), float(d)

        # print exspected output
        print(Box(l, w, d))
