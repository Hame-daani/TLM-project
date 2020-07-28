from numpy.lib.arraysetops import unique


class Wing():

    def __init__(self, string):
        #TODO: its_terminal
        from MyModule.funcs import its_terminal, its_variable
        # all lower letters are terminal
        self.terminals = [c for c in string if c.islower()]
        self.terminals = list(unique(self.terminals))
        # all upper letters are variable
        self.variables = [c for c in string if c.isupper()]
        self.variables = list(unique(self.variables))
        self.form = string

    def __str__(self):
        return self.form

    def __repr__(self):
        return self.form

    def __len__(self):
        return len(self.form)
