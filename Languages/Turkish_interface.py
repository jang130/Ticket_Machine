from error_classes import WrongOptionError


class TR:
    def __init__(self, operation):
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Zaman: {time} Tarih: {date}'

    def menu(self):
        self.operation.clear_console()
        print(self.date)
        print('Bilet Makinesi\nBir seçeneği seç: ')
        print('1. Kağıt bilet satın al\n2. Uzun süreli bilet al')
        print('3. Bilet tükenme tarihine bak\n4. Kaynaklara bak')
        print('5. Bakiye yüklenebilir biletlere bak:')
        print('6. Problem bildir\n7. Bitir')

    def paper_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Bilet tipini seç:')
        print('1. 20 dakikalık\n2. 75 dakikalık\n3. 24 saatlik\n4. 72 saatlik')

    def time_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Bilet tipini seç:')
        print('1. Aylık\n2. 3 Aylık')
        print('3. Yıllık')

    def personal_data(self, type_of_name):
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
        self.operation.clear_console()
        print(self.date)
        print('Biletin son geçerlilik tarihi:')
        print(expiry)

    def operation_done(self):
        self.operation.clear_console()
        print(self.date)
        print('Satın alımı başarılı.')

    def prepaid_check(self, prepaid_tickets):
        self.operation.clear_console()
        print(self.date)
        output = ''
        for ticket in prepaid_tickets:
            index = prepaid_tickets.index(ticket)
            output += f'{prepaid_tickets[index]}zł\n'
        print('Mevcut Biletler:')
        print(output)

    def funds_check(self, funds):
        self.operation.clear_console()
        print(self.date)
        print(f'Mevcut Kaynaklar: {funds[0]}.{funds[1]} zł')

    def terminate(self):
        self.operation.clear_console()
        print(self.date)
        print('İşlem sonlandı.')

    def problem_report(self):
        self.operation.clear_console()
        print(self.date)
        print('Lütfen hata mesajını giriniz:')

    '''
    Errors
    '''
    def WrongOption(self):
        self.operation.clear_console()
        print('Seçim hatalı')

    def MissingFile(self):
        self.operation.clear_console()
        print('Veritabanı dosyası eksik')

    def TimeTicketExists(self):
        self.operation.clear_console()
        print('Zamanlı bileti çoktan var')

    def NotEnoughFunds(self):
        self.operation.clear_console()
        print('Kaynaklar yetersiz')

    def CustomerNotFound(self):
        self.operation.clear_console()
        print('Müşteri veritabanında bulunmuyor.')

    def TicketDoesNotExist(self):
        self.operation.clear_console()
        print('Bilet mevcut değil')
