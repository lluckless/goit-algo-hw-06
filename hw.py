from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        
class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)    
    
    def is_valid_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    #Реалізація методу додавання телефону
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    #Реалізація методу видалення телефону
    def remove_phone(self, phone):
        putin = self.find_phone(phone)
        if putin in self.phones:
            self.phones.remove(putin)
    #Реалізація методу редагування телефону
    def edit_phone(self, old_phone, new_phone):
        getmanb = self.find_phone(old_phone) 
        # index = self.phones.index(getmanb)
        self.phones[self.phones.index(getmanb)] = Phone(new_phone)
    #Реалізація методу пошуку телефону
    def find_phone(self, phone):
        for pho in self.phones:
            if phone == pho.value:
                return pho
        return None
       
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    #Реалізація методу додавання до data
    def add_record(self, record):
        self.data[record.name.value] = record
    #Реалізація методу пошуку телефону за ім'ям in data
    def find(self, name):
        return self.data[name]

    #Реалізація методу видалення з data
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890","1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    for name, record in book.data.items():
        print(record)
