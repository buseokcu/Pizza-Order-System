import csv
import datetime
        

# main fonksiyonu (menüyü çağırır)
def main():
    f = open('Menu.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

# pizzanın açıklamasının okunması
    def get_description(self):
        return self.description
    
# pizzanın fiyatın okunması    
    def get_cost(self):
        return self.cost
    
# pizza çeşitleri, alt sınıfları
class KlasikPizza(Pizza):
    # pizzanın adı ve fiyatı
    def __init__(self):
        super().__init__('Klasik Pizza', 40.0)

class Margherita(Pizza):
    def __init__(self):
        super().__init__('Margherita Pizza', 50.0)

class Neapolitan(Pizza):
    def __init__(self):
        super().__init__('Neapolitan Pizza', 55.0)

class Hawaiian(Pizza):
    def __init__(self):
        super().__init__('Hawaiian Pizza', 60.0)

class Decorator(Pizza):
    def __init__(self, component, 
description, cost):
        self.description = description
        self.cost = cost
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + \
        + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + \
        ' ' + Pizza.get_description(self)
    
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Zeytinli', 5.0)

class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mantarlı', 3.0)

class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Keçi Peynirli', 10.0)

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Etli', 20.0)

class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Soğan', 6.0)

class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mısır', 7.0)

# main foksiyonu çağırılması (menünün yazılması)
if __name__ == '__main__':
    main()

while True:
    pizza_choice = int(input('Lütfen bir pizza türü seçiniz (1-4): '))
    if pizza_choice == 1:
        pizza = KlasikPizza()
        break
    elif pizza_choice == 2:
        pizza = Margherita()
        break
    elif pizza_choice == 3:
        pizza = Neapolitan()
        break
    elif pizza_choice == 4:
        pizza = Hawaiian()
        break
    else:
        print('Geçersiz bir kod girdiniz, lütfen tekrar deneyin.\n')

while True:
    sauce_choice = int(input('Lütfen pizzanız için bir adet malzeme seçiniz (11-16): '))

    if sauce_choice == 11:
        sauce = Zeytin(pizza)
        break
    elif sauce_choice == 12:
        sauce = Mantar(pizza)
        break
    elif sauce_choice == 13:
        sauce = KeciPeyniri(pizza)
        break
    elif sauce_choice == 14:
        sauce = Et(pizza)
        break
    elif sauce_choice == 15:
        sauce = Sogan(pizza)
        break
    elif sauce_choice == 16:
        sauce = Misir(pizza)
        break
    else:
        print('Geçersiz bir kod girdiniz, lütfen tekrar deneyin.\n')

total_cost = sauce.get_cost()

print(f'\nSeçiminiz: {sauce.get_description()}\nToplam fiyat: {total_cost:.2f} TL\n')

approval = input('Siparişi Onayla (e/h)')

if approval == 'e':
    name = input('\nLütfen isminizi giriniz: ')

    while True:
        try:
            id_num = int(input('Lütfen TC kimlik numaranızı giriniz: '))
            if len(str(id_num)) == 11:
                break
            else:
                print('TC kimlik numarası 11 haneli ve rakamlardan oluşmalıdır\n')
        except:
            print('TC kimlik numarası 11 haneli ve rakamlardan oluşmalıdır\n')

   # CC no denetimi yap doğru değil ise tekrar sor        
    while True:
        try:
            cc_num = int(input('Lütfen kredi kartı numaranızı giriniz: '))
            if len(str(cc_num)) == 16:
                break
            else:
                print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')
        except:
            print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')

    while True:
        try:
            cc_pass = int(input('Lütfen kredi kartı şifrenizi giriniz: '))
            if len(str(cc_pass)) == 4:
                break
            else:
                print('Kart numarası 4 haneli ve rakamlardan oluşmalıdır\n')
        except:
            print('Kart numarası 4 haneli ve rakamlardan oluşmalıdır\n')
        
    print(f'\nTeşekkürler {name}! {sauce.get_description()} siparişiniz alınmıştır.')
    print(f'Toplam tutar: {total_cost:.2f} TL')

# şuanın tarihini al ve formata uygun hale getir
    now = datetime.datetime.now()
    dt_str = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # csv dosyasını aç eğer yok ise oluştur ve kullanıcı bilgilerini, siparişi, tutarı ve zamanı yaz
    with open('Orders_Database.csv', 'a') as info_file:
        db_writer = csv.writer(info_file)
        db_writer.writerow([name, id_num, sauce.get_description(), total_cost, cc_num, cc_pass, dt_str])
    
# onay verilmez ise iptal et ve çık
else:
    print('Seçiminiz iptal edildi')
    exit


    
