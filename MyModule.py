from numpy.lib.arraysetops import unique


def loadGrammar(address):
    """Load a Grammar from text file.

    Arguments:
            address {string} -- address of text file

    Returns:
            Grammar -- grammar created by data
    """
    with open(address, 'r') as file:
        data = file.readlines()
        # clear each line from '\n'
        data = [d.replace("\n", "") for d in data]
        return Grammar(data)


class Grammar():

    def __init__(self, data):
        # create product from each line in data
        self.products = [Production(line) for line in data]
        # extract terminals and variables from products
        self.terminals = Production.getTerminals(self.products)
        self.variables = Production.getVariables(self.products)
        # first variable is our start variable
        self.start_var = self.variables[0]

    def __str__(self):
        return f"Variables: {self.variables}\nTerminals: {self.terminals}\nStart: {self.start_var}\nProducts: {self.products}"



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


class Wing():

    def __init__(self, string):
        # all lower letters are terminal
        self.terminals = [c for c in string if c.islower()]
        # all upper letters are variable
        self.variables = [c for c in string if c.isupper()]
        self.form = string

    def __str__(self):
        return self.form

    def __repr__(self):
        return self.form
