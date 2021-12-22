from system import WrongOptionError, choice
from english_interface import EN

def choose_language():
    print('Available languages: \n1.Polish\n2.English\n>')
    option = choice()
    if option == 1:
        return
        #polish()
        #language = PL()
    elif option == 2:
        english()
    else:
        raise WrongOptionError

def english():
    language = EN()
    language.text()



def polish():
    pass

choose_language()