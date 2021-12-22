class EN:
    def __init__(self):
        pass


    def text(self):
        print('Ticket Machine\n\r Choose an option: ')
        print('1.Language menu\n\r 2.Paper ticket purchase')
        print('3.Long term tickets purchase\n\r 4.Check ticket expiration')
        print('5.Check amout of funds\n\r 6.Report problem')
        print('>')
        return self.options(input())

    def options(self, input):
        if input == '1':
            return True
        elif input == '2':
            pass
        elif input == '3':
            pass
        elif input == '4':
            pass
        elif input == '5':
            pass
        elif input == '6':
            pass

interface = EN()
print(interface.text())