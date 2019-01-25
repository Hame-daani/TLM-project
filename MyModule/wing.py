
class Wing():

    def __init__(self, string):
        #TODO: its_terminal
        from MyModule.funcs import its_terminal, its_variable
        # all lower letters are terminal
        self.terminals = [c for c in string if c.islower()]
        # all upper letters are variable
        self.variables = [c for c in string if c.isupper()]
        self.form = string

    def __str__(self):
        return self.form

    def __repr__(self):
        return self.form

    def __len__(self):
        return len(self.form)
