from system import WrongOptionError


class TR:
    def __init__(self, operation):
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Zaman: {time} Tarih: {date}'

    def menu(self):
        self.operation.clear_console()
        print(self.date)
        print('Bilet Makinesi\n\rBir seçeneği seç: ')
        print('1. Kağıt bilet satın al\n\r2. Uzun süreli bilet al')
        print('3. Bilet tükenme tarihine bak\n\r4. Kaynaklara bak')
        print('5. Problem bildir\n\r6. Bitir')

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

    def prepaid_check(self, funds):
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

