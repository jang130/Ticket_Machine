import english_interface
import polish_interface
from system import WrongOptionError, choice


def choose_language():
    print('Available languages: \n1.Polish\n2.English\n>')
    option = choice()
    if option == 1:
        #polish()
        pass
    elif option == 2:
        english()
    else:
        raise WrongOptionError

def english():
    language = english_interface.EN()
    language.text()


'''
def polish():
    language = polish_interface.PL()
    language.text()
'''
choose_language()