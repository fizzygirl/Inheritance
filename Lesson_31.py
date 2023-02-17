'''Задание 1
Создайте класс Device, который содержит информа-
цию об устройстве.
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы.'''


class Device:
    __category = 'Kitchen appliances'
    __energy_dependent = 'Yes'
    __scope_of_use = 'Domestic'
    name = 'Kitchen device'
    color = 'White'
    case_material = 'Plastic'
    weight = '2kg'
    power = '1000W'
    price = '0grn'

    def work_mode(self):
        print("Works")

    def mode(self):
        print('Standby mode')

    def power_mode(self):
        print('Power on')

    def change_power_mode(self, power_mode_off):
        self.power_mode = power_mode_off
        print('Power off')

    def change_name(self, new_name):
        self.name = new_name

    def change_color(self, new_color):
        self.color = new_color

    def change_case_material(self, new_case_material):
        self.case_material = new_case_material

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_power(self, new_power):
        self.power = new_power

    def change_price(self, new_price):
        self.price = new_price


class CoffeeMachine(Device):
    name = 'Delonghi'
    color = 'Black'
    case_material = 'Plastic'
    container = 'Milk container'
    used_coffee = 'Grain, Milled'
    power = '1450W'
    type = 'Automatic'
    weight = '9kg'
    price = '16 000grn'

    def cooking_coffe(self):
        print('Making coffee')

    def cooking_cappuccino(self):
        print('Making cappuccino')

    def add_sugar(self):
        print('Added sugar')

    def heating(self):
        print('Cup heating')

    def descaling(self):
        print('Cleaning from scale')

    def reminder(self):
        print('Reminder to rinse the cappuccinatore')

    def change_container(self, new_container):
        self.container = new_container

    def change_used_coffee(self, new_coffee):
        self.used_coffee = new_coffee

    def change_type(self, new_type):
        self.type = new_type

    def __str__(self):
        return f'Name : {self.name},\nColor : {self.color},\nCase material : {self.case_material},' \
               f'\nContainer : {self.container},\nUsed coffee : {self.used_coffee},' \
               f'\nPower : {self.power},\nType : {self.type},\nWeight : {self.weight},\nPrice : {self.price}'

class Blender(Device):
    name = 'Bosh'
    color = 'Black'
    case_material = 'Plastic'
    weight = '0.7kg'
    glass_capacity = '700ml'
    type = 'Submersible'
    nozzle = 'Mini grinder'
    number_of_speeds = '1'
    foot_material = 'Metal'
    power = '600W'
    price = '1 600grn'

    def grinds(self):
        print('Grinds ingredients')

    def whips(self):
        print('Whips ingredients')

    def change_type(self, new_type):
        self.type = new_type

    def change_glass_capacity(self, new_glass_capacity):
        self.glass_capacity = new_glass_capacity

    def change_nozzle(self, new_nozzle):
        self.nozzle = self.nozzle + ', '+ new_nozzle

    def change_number_of_speeds(self, new_speeds):
        self.number_of_speeds = new_speeds

    def change_foot_material(self, new_foot_material):
        self.foot_material = new_foot_material

    def __str__(self):
        return f'Name : {self.name},\nColor : {self.color},\nCase material : {self.case_material},' \
               f'\nPower : {self.power},\nType : {self.type},\nWeight : {self.weight},' \
               f'\nGlass capacity : {self.glass_capacity},\nNozzle : {self.nozzle},' \
               f'\nNumber of speeds : {self.number_of_speeds},\nFoot material : {self.foot_material},\nPrice : {self.price}'

class MeatGrinder(Device):
    name = 'Bosh'
    color = 'Black and White'
    case_material = 'Plastic'
    weight = '4.6kg'
    power = '1600W'
    performance = '1.8 kg/min'
    nozzle_quantity = '3'
    nozzle = 'For sausages, For grater/shredder, Kebbe'
    number_of_grids = '3'
    extra_features = 'Storage compartment for accessories and discs, Reverse'
    additional_features = 'Reversible knife, Carry handle, Rubber feet'
    price = '4 600grn'

    def chop(self):
        print('Minced meat')

    def rub(self):
        print('Rubbed ingredients')

    def made_juice(self):
        print('Tomato juice')

    def change_performance(self, new_performance):
        self.performance = new_performance

    def change_nozzle(self, new_nozzle):
        self.nozzle = self.nozzle + ', ' + new_nozzle

    def change_nozzle_quantity(self, new_nozzle_quantity):
        self.nozzle_quantity = new_nozzle_quantity

    def change_number_of_grids(self, new_number_of_grids):
        self.number_of_grids = new_number_of_grids

    def change_extra_features(self, new_extra_features):
        self.extra_features = new_extra_features

    def change_additional_features(self, new_additional_features):
        self.additional_features = new_additional_features

    def __str__(self):
        return f'Name : {self.name},\nColor : {self.color},\nCase material : {self.case_material},' \
               f'\nPower : {self.power},\nPerformance : {self.performance},\nWeight : {self.weight},' \
               f'\nNozzle quantity : {self.nozzle_quantity},\nNozzle : {self.nozzle},' \
               f'\nNumber of grids : {self.number_of_grids},\nExtra features : {self.extra_features}' \
               f'\nAdditional features : {self.additional_features},\nPrice : {self.price}'

default_device = Device()
default_device.mode()
default_device.power_mode()
default_device.change_power_mode(1)

print(CoffeeMachine())
my_CoffeeMachine = CoffeeMachine()
print()
my_CoffeeMachine.mode()
my_CoffeeMachine.cooking_cappuccino()
my_CoffeeMachine.add_sugar()
my_CoffeeMachine.change_name('Philips')
my_CoffeeMachine.change_color('Red')
my_CoffeeMachine.change_case_material('Metal')
my_CoffeeMachine.change_weight('7kg')
my_CoffeeMachine.change_power('1500W')
my_CoffeeMachine.change_container('No milk container')
my_CoffeeMachine.change_price('11 000grn')
print(my_CoffeeMachine)

my_blender = Blender()
my_blender.power_mode()
my_blender.mode()
my_blender.grinds()
my_blender.change_name('Phillips')
my_blender.change_color('Silver')
my_blender.change_weight('1.9kg')
my_blender.change_power('800W')
my_blender.change_glass_capacity('1000ml')
my_blender.change_nozzle('Whisk, Spiralizer')
my_blender.change_number_of_speeds('8')
my_blender.change_price('3 100grn')
print(my_blender)

my_MeatGrinder = MeatGrinder()
my_MeatGrinder.change_name('MOULINEX')
my_MeatGrinder.change_color('White')
my_MeatGrinder.change_weight('2.3kg')
my_MeatGrinder.change_power('1400')
my_MeatGrinder.change_performance('1.7kg/min')
my_MeatGrinder.change_nozzle_quantity('2')
my_MeatGrinder.change_nozzle('For sausages')
my_MeatGrinder.change_extra_features('Self-sharpening knife, Handle for easy transport')
my_MeatGrinder.change_price('3 000grn')
my_MeatGrinder.power_mode()
my_MeatGrinder.work_mode()
my_MeatGrinder.chop()
print(my_MeatGrinder)


'''Задание 2
Создайте класс Ship, который содержит информацию
о корабле.
С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс
Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые
для работы методы.'''

class Ship:
    __category = 'Military watercraft'
    __vehicle = 'Ship'
    name = 'No'
    year = 'No'
    country = 'No'
    weight = 'No'
    length = 'No'
    width = 'No'
    speed = 'No'
    crew = 'No'
    swimming_area = 'Open sea'
    way_of_moving = 'Overwater'

    def mode(self):
        print('Patrolling mode')

    def change_name(self, new_name):
        self.name = new_name

    def change_year(self, new_year):
        self.year = new_year

    def change_country(self,new_country):
        self.country = new_country

    def change_weight(self, new_weight):
        self.case_weight = new_weight

    def change_length(self, new_length):
        self.length = new_length

    def change_width(self, new_width):
        self.width = new_width

    def change_speed(self, new_speed):
        self.speed = new_speed

    def change_crew(self, new_crew):
        self.crew = new_crew

    def change_swimming_area(self, new_swimming_area):
        self.swimming_area = new_swimming_area

    def change_way_of_moving(self, new_way_of_moving):
        self.way_of_moving = new_way_of_moving


class Frigate(Ship):
    name = 'Hetman Sahaidachny'
    year = '1993'
    country = 'Ukraine'
    weight = '3 600ton'
    length = '122m'
    width = '14m'
    speed = '31nodes'
    crew = '198'
    swimming_area = 'Open sea'
    way_of_moving = 'Overwater'

    def patrol(self):
        print('Frigate is patrolling')

    def destroy(self):
        print('Destroy submarines')

    def guarding(self):
        print('Guarding ships and vessels at sea')

    def defence(self):
        print('Air defense')

    def attack(self):
        print('Attack ground target')

    def __str__(self):
        return f'Name : {self.name},\nYear : {self.year},\nCountry : {self.country},\nWeight : {self.weight},' \
               f'\nLength : {self.length},\nWidth : {self.width},\nSpeed : {self.speed},\nCrew : {self.crew},' \
               f'\nSwimming area : {self.swimming_area},\nWay of moving : {self.way_of_moving}'

class Destroyer(Ship):
    name = 'Lassen'
    year = '1999'
    country = 'USA'
    weight = '6 950ton'
    length = '155m'
    width = '20m'
    speed = '32nodes'
    crew = '380'
    swimming_area = 'Open sea'
    way_of_moving = 'Overwater'

    def destroy_submarines(self):
        print('Destroy submarines')

    def destroy_ships(self):
        print('Descent of surface ships')

    def destroy_flight(self):
        print('Fight with lethal devices')

    def protection(self):
        print('Protection of own ships')

    def min(self):
        print('Min installed')

    def patrol(self):
        print('Destroyer is patrolling')

    def exploration(self):
        print('Intelligence service')

    def support(self):
        print('Fire support for landing forces')

    def __str__(self):
        return f'Name : {self.name},\nYear : {self.year},\nCountry : {self.country},\nWeight : {self.weight},\nLength : {self.length},' \
               f'\nWidth : {self.width},\nSpeed : {self.speed},\nCrew : {self.crew},' \
               f'\nSwimming area : {self.swimming_area},\nWay of moving : {self.way_of_moving}'

class Cruiser(Ship):
    name = 'Moskva'
    year = '1979'
    country = 'SRSR'
    weight = '11 000ton'
    length = '180m'
    width = '42,5m'
    speed = '32,5nodes'
    crew = '485'
    swimming_area = 'Open sea'
    way_of_moving = 'Overwater'

    def landing(self):
        print('Landing of amphibious assault')

    def min(self):
        print('Setting up minefields')

    def defence(self):
        print('Defense of warship formations')

    def support(self):
        print('Fire support for coastal flanks of ground forces')

    def __str__(self):
        return f'Name : {self.name},\nYear : {self.year},\nCountry : {self.country},\nWeight : {self.weight},' \
               f'\nLength : {self.length},\nWidth : {self.width},\nSpeed : {self.speed},\nCrew : {self.crew},' \
               f'\nSwimming area : {self.swimming_area},\nWay of moving : {self.way_of_moving}'

my_ship = Frigate()
my_ship.mode()
my_ship.patrol()
my_ship.guarding()
my_ship.change_name('Mykolaiv')
print(my_ship)

destroyer_ship = Destroyer()
destroyer_ship.protection()
destroyer_ship.support()
destroyer_ship.change_country('England')
print(destroyer_ship)

big_ship = Cruiser()
big_ship.min()
big_ship.landing()
big_ship.change_name('Ticonderoga')
print(big_ship)


'''Задание 3
Запрограммируйте класс Money (объект класса опе-
рирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для хра-
нения целой части денег (доллары, евро, гривны и т.д.) и
поле для хранения копеек (центы, евроценты, копейки
и т.д.).
Реализовать методы для вывода суммы на экран, за-
дания значений для частей.'''

class Money:
    whole = '15'
    currency = 'UAH'
    pennies = '50'
    name_of_pennies = 'kop'

    def choose_money(self):
        new_whole = input('Enter whole : ')
        self.whole = new_whole
        new_currency = input('Enter name of currency : ')
        self.currency = new_currency
        new_pennies = input('Enter pennies : ')
        self.pennies = new_pennies
        new_name_pennies = input('Enter the name of currency pennie : ')
        self.name_of_pennies = new_name_pennies

    def __str__(self):
        return f'Your money : {self.whole} {self.currency}, {self.pennies} {self.name_of_pennies}'

hryvnia_money = Money()
print(hryvnia_money)
hryvnia_money.choose_money()
print(hryvnia_money)




