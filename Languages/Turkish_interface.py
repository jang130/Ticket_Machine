from error_classes import WrongOptionError


class TR:
    def __init__(self, operation):
        '''
        Class that prints messages in Turkish.
        And sets formatted time and date variable.

        :param operation:
        :type object:
        '''
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Zaman: {time} Tarih: {date}'

    def menu(self):
        '''
        Prints main option menu.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Bilet Makinesi\nBir seçeneği seç: ')
        print('1. Kağıt bilet satın al\n2. Uzun süreli bilet al')
        print('3. Bilet tükenme tarihine bak\n4. Kaynaklara bak')
        print('5. Bakiye yüklenebilir biletlere bak:')
        print('6. Problem bildir\n7. Bitir')

    def paper_ticket_type(self):
        '''
        Prints chooice of paper ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Bilet tipini seç:')
        print('1. 20 dakikalık\n2. 75 dakikalık\n3. 24 saatlik\n4. 72 saatlik')

    def time_ticket_type(self):
        '''
        Prints chooice of time ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Bilet tipini seç:')
        print('1. Aylık\n2. 3 Aylık')
        print('3. Yıllık')

    def personal_data(self, type_of_name):
        '''
        Prints information about inputting
        first name and last name.
        '''
        self.operation.clear_console()
        print(self.date)
        if type_of_name == 'first':
            print('İsmini gir:')
        elif type_of_name == 'last':
            print('Soyadını gir:')
        else:
            raise WrongOptionError
        return

    def check_ticket(self, expiry):
        '''
        Prints ticket expiry date.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Biletin son geçerlilik tarihi:')
        print(expiry)

    def operation_done(self):
        '''
        Prints information that operation
        has been done.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Satın alımı başarılı.')

    def prepaid_check(self, prepaid_tickets):
        '''
        Prints available prepaid tickets.
        '''
        self.operation.clear_console()
        print(self.date)
        output = ''
        for ticket in prepaid_tickets:
            index = prepaid_tickets.index(ticket)
            output += f'{prepaid_tickets[index]}zł\n'
        print('Mevcut Biletler:')
        print(output)

    def funds_check(self, funds):
        '''
        Prints avialable customer funds.
        '''
        self.operation.clear_console()
        print(self.date)
        print(f'Mevcut Kaynaklar: {funds[0]}.{funds[1]} zł')

    def terminate(self):
        '''
        Prints information about
        terminating sesion.
        '''
        self.operation.clear_console()
        print(self.date)
        print('İşlem sonlandı.')

    def problem_report(self):
        '''
        Prints request to describe problem.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Lütfen hata mesajını giriniz:')

    '''
    Errors
    '''
    def WrongOption(self):
        '''
        Prints error that choosen option
        is wrong.
        '''
        self.operation.clear_console()
        print('Seçim hatalı')

    def MissingFile(self):
        '''
        Prints error that file not found.
        '''
        self.operation.clear_console()
        print('Veritabanı dosyası eksik')

    def TimeTicketExists(self):
        '''
        Prints error that time ticket
        is already in customers data.
        '''
        self.operation.clear_console()
        print('Zamanlı bileti çoktan var')

    def NotEnoughFunds(self):
        '''
        Prints error that customer have
        insufficient funds.
        '''
        self.operation.clear_console()
        print('Kaynaklar yetersiz')

    def CustomerNotFound(self):
        '''
        Prints error that customer is
        not in the database.
        '''
        self.operation.clear_console()
        print('Müşteri veritabanında bulunmuyor.')

    def TicketDoesNotExist(self):
        '''
        Prints error that ticket not found.
        '''
        self.operation.clear_console()
        print('Bilet mevcut değil')
