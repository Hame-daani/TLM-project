from MyModule.production import Production
from MyModule.parser import DepthParser, BreadthParser
from numpy.lib.arraysetops import unique


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
        self.breadth_parser = BreadthParser(
            self.start_var, self.products, self.variables)

    def __str__(self):
        return f"Variables: {self.variables}\nTerminals: {self.terminals}\nStart: {self.start_var}\nProducts: {self.products}"

    def __len__(self):
        return len(self.products)

    def detect_problem(self):
        landa = self.detect_landa()
        unit = self.detect_unit()
        useless = self.detect_useless()
        return (landa, unit, useless)

    def detect_landa(self):
        landas = []
        for p in self.products:
            if '$' in p.right_wing.form:
                landas.extend(p.left_wing.variables)
        return None if len(landas) == 0 else landas

    def detect_unit(self):
        units = []
        for p in self.products:
            if len(p.right_wing.form) == 1 and len(p.right_wing.variables) == 1:
                units.append(
                    (p.left_wing.variables[0], p.right_wing.variables[0]))
        return None if len(units) == 0 else units

    def detect_useless(self):
        useless = []
        usefulls = [self.start_var]
        for u in usefulls:
            for p in self.products:
                if p.left_wing.variables[0] == u:
                    for v in p.right_wing.variables:
                        if v not in usefulls:
                            usefulls.append(v)
        for v in self.variables:
            if v not in usefulls:
                useless.extend(v)
        return None if len(useless) == 0 else useless
