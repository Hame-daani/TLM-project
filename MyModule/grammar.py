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
        self.start_var = 'S'
        self.depth_parser = None
        self.breadth_parser = None

    def __str__(self):
        return f"Variables: {self.variables}\nTerminals: {self.terminals}\nStart: {self.start_var}\nProducts: {self.products}"

    def __len__(self):
        return len(self.products)

    def its_simple(self):
        from MyModule.funcs import its_terminal, its_variable
        occurens = []
        for p in self.products:
            if len(p.right_wing.terminals) > 1:
                return False
            if len(p.right_wing.terminals) == 1 and not its_terminal(p.right_wing.form[0]):
                return False
            o = (p.left_wing.variables[0], p.right_wing.terminals[0])
            if o in occurens:
                return False
            else:
                occurens.append(o)
        return True

    def depth_parse(self, target):
        dp = DepthParser(self.start_var, self.products, self.variables)
        return dp.parse(target)

    def breadth_parse(self, target):
        bp = BreadthParser(self.start_var, self.products, self.variables)
        return bp.parse(target)

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

    def normalize(self):
        landas = self.detect_landa()
        while landas:
            self.remove_landa(landas)
            landas = self.detect_landa()
        units = self.detect_unit()
        while units:
            self.remove_units(units)
            units = self.detect_unit()
        useless = self.detect_useless()
        while useless:
            self.remove_useless(useless)
            useless = self.detect_useless()

    def remove_landa(self, landas):
        for l in landas:
            for p in self.products:
                if p.left_wing.variables[0] == l and p.right_wing.form == "$":
                    self.products.remove(p)
                if l in p.right_wing.variables:
                    new_p = p.right_wing.form.replace(l, "")
                    if new_p:
                        self.products.append(Production(
                            f"{p.left_wing.form}->{new_p}"))

    def remove_units(self, units):
        for left, right in units:
            products = []
            for p in self.products:
                if len(p.right_wing.form) == 1 and p.left_wing.variables[0] == left and p.right_wing.variables[0] == right:
                    self.products.remove(p)
            for p in self.products:
                if p.left_wing.variables[0] == right:
                    products.append(p)

            for p in products:
                self.products.append(Production(
                    f"{left}->{p.right_wing.form}"))

    def remove_useless(self, useless):
        pass

    def to_chomskey(self):
        self.remove_s_rhs()
        self.normalize()
        self.var_for_ter()
        self.split_two_more()

    def remove_s_rhs(self):
        for p in self.products:
            if self.start_var in p.right_wing.variables:
                self.products.insert(0, Production(f"T->{self.start_var}"))
                self.variables.append("T")
                self.start_var = "T"
                break

    def var_for_ter(self):
        from MyModule.funcs import its_terminal, its_variable
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table = {}
        for t in self.terminals:
            table[t] = None
        for p in self.products:
            if len(p.right_wing.form) > 1 and len(p.right_wing.terminals) >= 1:
                for c in p.right_wing.form:
                    if its_terminal(c):
                        if table[c] == None:
                            for l in letters:
                                if l not in self.variables:
                                    table[c] = l
                                    self.products.append(
                                        Production(f"{l}->{c}"))
                                    if l not in self.variables:
                                        self.variables.append(l)
                                    break
                        p.right_wing.form = p.right_wing.form.replace(
                            c, table[c])
                        p.form = p.form.replace(c, table[c])
                        if table[c] not in p.right_wing.variables:
                            p.right_wing.variables.append(table[c])
                        if table[c] not in p.variables:
                            p.variables.append(table[c])
                        try:
                            p.right_wing.terminals.remove(c)
                        except ValueError:
                            pass
                        try:
                            p.terminals.remove(c)
                        except ValueError:
                            pass

    def split_two_more(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for p in self.products:
            if len(p.right_wing.form) > 2:
                for l in letters:
                    if l not in self.variables:
                        new_p_value = p.right_wing.form[1:]
                        self.variables.append(l)
                        self.products.append(Production(f"{l}->{new_p_value}"))
                        p.right_wing.form = p.right_wing.form.replace(
                            new_p_value, l)
                        p.form = p.form.replace(new_p_value, l)
                        p.variables.append(l)
                        p.right_wing.variables.append(l)
                        for c in new_p_value:
                            p.variables.remove(c)
                            p.right_wing.variables.remove(c)
                        break
