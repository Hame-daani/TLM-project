from MyModule.production import getProducts


def getTable(products, variables):
    table = {}
    for v in variables:
        vProducts = getProducts(v, products)
        table[v] = vProducts
    return table


class Parser():

    def __init__(self, start_var, products, variables):
        self.start_var = start_var
        # table of each 'variable' and its 'productions'
        self.table = getTable(products, variables)


class DepthParser(Parser):

    def __init__(self, start_var, products, variables):
        return super().__init__(start_var, products, variables)

    def parse(self, target):
        from MyModule.funcs import its_terminal, its_variable
        start = Node(self.start_var, target, " ", None)
        for p in self.table[start.value]:
            start.childs.append(Node(p, target, start.value+"->"+p, start))
            if self.parse_inside(start.childs[-1]):
                start.valid = True
                return (start, True)
        return (start, False)

    def parse_inside(self, node):
        from MyModule.funcs import its_terminal, its_variable
        if not node.its_valid():
            node.valid = False
            return False
        if node.its_match():
            node.valid = True
            return True
        for c in node.value:
            if its_variable(c):
                for p in self.table[c]:
                    new_value = node.value.replace(c, p, 1)
                    node.childs.append(
                        Node(new_value, node.target, c+"->" + p, node))
                    if self.parse_inside(node.childs[-1]):
                        node.valid = True
                        return True
        return False


class BreadthParser(Parser):

    def __init__(self, start_var, products, variables):
        self.stack = []
        return super().__init__(start_var, products, variables)

    def parse(self, target):
        from MyModule.funcs import its_terminal, its_variable
        start = Node(self.start_var, target, " ", None)
        for p in self.table[start.value]:
            nc = Node(p, target, start.value+"->"+p, start)
            start.childs.append(nc)
            self.stack.append(nc)
        while self.stack:
            if self.parse_inside(self.stack.pop(0)):
                return (start, True)

        return (start, False)

    def parse_inside(self, node):
        from MyModule.funcs import its_terminal, its_variable
        if not node.its_valid():
            node.valid = False
            return False
        if node.its_match():
            node.valid_it()
            return True
        for c in node.value:
            if its_variable(c):
                for p in self.table[c]:
                    new_value = node.value.replace(c, p, 1)
                    nc = Node(new_value, node.target, c+"->" + p, node)
                    node.childs.append(nc)
                    if nc.its_match():
                        nc.valid_it()
                        return True
                    self.stack.append(nc)
        return False


class Node():

    def __init__(self, value, target, p, parent):
        self.p = p
        self.parent = parent
        self.valid = None
        self.value = value
        self.target = target
        self.childs = []

    def its_valid(self):
        if len(self.target) < len(self.value):
            return False
        from MyModule.funcs import its_terminal, its_variable
        for i in range(0, len(self.value)):
            if its_variable(self.value[i]):
                break
            if self.value[i] != self.target[i]:
                return False
        for i in range(-1, len(self.value)*-1, -1):
            if its_variable(self.value[i]):
                break
            if self.value[i] != self.target[i]:
                return False
        return True

    def its_match(self):
        return self.value == self.target

    def valid_it(self):
        self.valid = True
        if self.parent:
            self.parent.valid_it()
