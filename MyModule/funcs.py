from MyModule.grammar import Grammar


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

# TODO: add '__len__' to classes

# TODO: add 'its_terminal' and 'its_variable' funcs.
