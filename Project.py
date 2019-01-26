import os
from MyModule.funcs import loadGrammar
from nltk.tree import Tree
from colorama import Fore, Style

print_unvalid = False
# TODO: add flag for unvalid nodes


def tostring(node):
    string = "("
    if node.valid == True:
        string += node.p+":{"+node.value+"}"
    else:
        # to remove
        string += "#"+node.p+":{"+node.value+"}#"

    for c in node.childs:
        if c.childs:
            string += tostring(c)
        else:
            pass
            if c.valid == True:
                string += " ***"+c.p+":{"+c.value+"}***"
            else:
                # to remove
                string += " #"+c.p+":{"+c.value + \
                    "}#" if print_unvalid else " ##"

    string += ")"
    return string


def menu():
    s = """
    1. Print Grammar
    2. Test if it's S_Grammar
    3. Depth_First_Parsing
    4. Breadth_First_Parsing
    5. CYK Parsing
    6. S_Parser
    7. Normalize
    8. Convert To Chomskey
    9. Exit"""
    print(Fore.YELLOW + s + Fore.RESET)


if __name__ == "__main__":
    g = loadGrammar(os.sys.argv[1])
    landa, unit, useless = g.detect_problem()
    if landa or unit or useless:
        print(Fore.RED+"Grammar had problem!!!!!")
        if landa:
            print("Landa: ", landa)
        if unit:
            print("Unit: ", unit)
        if useless:
            print("useless: ", useless)
        print(Fore.RESET)
    option = 0
    while option != 9:
        menu()
        option = int(input("Select Option: "))
        if option == 1:
            print(Fore.GREEN)
            print(g)
            print(Fore.RESET)
        if option == 2:
            s = Fore.GREEN+"YES, its simple," if g.its_simple() else Fore.RED + \
                "NO, its NOT simple"
            print(s+Fore.RESET)
        if option == 3:
            target = input("Insert the target: ")
            node, result = g.depth_parse(target)
            if result:
                print(Fore.GREEN+"Sucess!!"+Fore.RESET)
                print_unvalid = input(
                    "Do you want to print unvalid nodes?(y,n)")
                print_unvalid = True if print_unvalid == 'y' else False
                print("Drawing Tree ....")
                tree = Tree.fromstring(tostring(node))
                tree.draw()
            else:
                print(Fore.RED+"Failed!!"+Fore.RESET)
        if option == 4:
                                                            # TODO:breadth had problem !!!!
            target = input("Insert the target: ")
            node, result = g.breadth_parse(target)
            if result:
                print(Fore.GREEN+"Sucess!!"+Fore.RESET)
                print_unvalid = input(
                    "Do you want to print unvalid nodes?(y,n)")
                print_unvalid = True if print_unvalid == 'y' else False
                print("Drawing Tree ....")
                tree = Tree.fromstring(tostring(node))
                tree.draw()
            else:
                print(Fore.RED+"Failed!!"+Fore.RESET)
        if option == 5:
            target = input("Insert the target: ")
            node, result = g.depth_parse(target)
            if result:
                print(Fore.GREEN+"Sucess!!"+Fore.RESET)
                print_unvalid = input(
                    "Do you want to print unvalid nodes?(y,n)")
                print_unvalid = True if print_unvalid == 'y' else False
                print("Drawing Tree ....")
                tree = Tree.fromstring(tostring(node))
                tree.draw()
            else:
                print(Fore.RED+"Failed!!"+Fore.RESET)
        if option == 6:
            target = input("Insert the target: ")
            node, result = g.s_parse(target)
            if result:
                print(Fore.GREEN+"Sucess!!"+Fore.RESET)
                print("Drawing Tree ....")
                tree = Tree.fromstring(tostring(node))
                tree.draw()
            else:
                print(Fore.RED+"Failed!!"+Fore.RESET)
        if option == 7:
            g.normalize()
            print(Fore.GREEN)
            print(g)
            print(Fore.RESET)
        if option == 8:
            g.to_chomskey()
            print(Fore.GREEN)
            print(g)
            print(Fore.RESET)
