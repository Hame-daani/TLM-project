from MyModule.wing import Wing
from numpy.lib.arraysetops import unique


class Production():

    def __init__(self, string):
        # split string from '->' and create two wing with each side
        left_side, right_side = string.split("->")
        self.left_wing = Wing(left_side)
        self.right_wing = Wing(right_side)
        # find uniqe terminals in both wing
        self.terminals = list(
            unique(self.right_wing.terminals + self.left_wing.terminals))
        # find uniqe variables in both side
        self.variables = list(
            unique(self.right_wing.variables + self.left_wing.variables))

        self.form = str(self)

    def __str__(self):
        return f"{self.left_wing}->{self.right_wing}"

    def __repr__(self):
        return f"{self.left_wing}->{self.right_wing}"

    def getTerminals(products):
        terminals = []
        for p in products:
            for t in p.terminals:
                if t not in terminals:
                    terminals.append(t)
        return terminals

    def getVariables(products):
        variables = []
        for p in products:
            for t in p.variables:
                if t not in variables:
                    variables.append(t)
        return variables

    def __len__(self):
        return (len(self.left_wing) + len(self.right_wing))
