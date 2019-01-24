from MyModule.production import Production
from MyModule.parser import DepthParser


class Grammar():

    def __init__(self, data):
        # create product from each line in data
        self.products = [Production(line) for line in data]
        # extract terminals and variables from products
        self.terminals = Production.getTerminals(self.products)
        self.variables = Production.getVariables(self.products)
        # first variable is our start variable
        self.start_var = self.variables[0]
        self.depth_parser = DepthParser(
            self.start_var, self.products, self.variables)

    def __str__(self):
        return f"Variables: {self.variables}\nTerminals: {self.terminals}\nStart: {self.start_var}\nProducts: {self.products}"

    def __len__(self):
        return len(self.products)
