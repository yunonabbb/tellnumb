# filename = input("Введите имя файла: ")
#
# with open(filename, 'w') as file:
#     file.write("hello pyy")


# import random
#
# filename = input("Введите имя файла: ")
#
# numbers = [random.randint(1, 100) for _ in range(10)]
# numbers_text = ', '.join(map(str, numbers))
#
# with open(filename, 'w') as file:
#     file.write(numbers_text)


# fileeee= input("Введите имя файла: ")
#
# with open(fileeee, 'r') as file:
#     numbers_text = file.read()
#
# numbers = list(map(int, numbers_text.split(',')))
# sum_of_numbers = sum(numbers)
#
# print("Сумма чисел:", sum_of_numbers)



# class PhoneBook:
#     def __init__(self):
#         self.contacts = {}
#
#     def add_contact(self, name, phone_numbers):
#         self.contacts[name] = set(phone_numbers)
#
#     def remove_contact(self, name):
#         if name in self.contacts:
#             del self.contacts[name]
#             print("Контакт успешно удален.")
#         else:
#             print("Контакт не найден.")
#
#     def get_phone_numbers(self, name):
#         if name in self.contacts:
#             return self.contacts[name]
#         else:
#             return None
#
#     def print_contacts(self):
#         if len(self.contacts) == 0:
#             print("Телефонная книга пуста.")
#         else:
#             for name, phone_numbers in self.contacts.items():
#                 print(f"ФИО: {name}")
#                 print("Номера телефона:", ', '.join(phone_numbers))
#                 print()
#
# phone_book = PhoneBook()
#
# phone_book.add_contact("кузнецова анастасия алексеевна", ["456797091", "978587947"])
# phone_book.add_contact("самопалова мария николаевна", ["708673689"])
#
# phone_book.print_contacts()

