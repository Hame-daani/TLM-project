from MyModule.grammar import Grammar


def loadGrammar(address):
    """Load a Grammar from text file.

    Arguments:
            address {string} -- address of text file

    Returns:
            Grammar -- grammar created by data
    """
    try:
        with open(address, 'r') as file:
            data = file.readlines()
            # clear each line from '\n'
            data = [d.replace("\n", "") for d in data]
            return Grammar(data)
    except FileNotFoundError as error:
        print(error)


def its_terminal(c):
    return c.islower()


def its_variable(c):
    return c.isupper()
