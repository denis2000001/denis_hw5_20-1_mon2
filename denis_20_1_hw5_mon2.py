import re
class ValidCarNumber:
    def __init__(self,number):
        self.number = number
    def is_valid(self):
        is_valid = re.search(r"0([0-9]{1})KG([0-9]{3}[A-Z]{2,3})", number)
        try:
            if number[is_valid.start():is_valid.end()] == number:
                return "IS valid number!"
        except:
            return "Is Invalid number!"
number = input("Введите номер: ")
num = ValidCarNumber(number)
print(num.is_valid())