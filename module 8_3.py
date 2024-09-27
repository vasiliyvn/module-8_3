class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message
class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)
        #Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    def __is_valid_vin(self,__vin):
        if not isinstance(self.__vin,int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True
        #Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    def __is_valid_numbers(self, __numbers):
        if not isinstance(self.__numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if len(__numbers) !=6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')