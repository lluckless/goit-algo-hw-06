
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
        super().__init__(value)
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
    #Валідація формату (10 цифр)     
    def is_valid_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    #Реалізація методу додавання телефону
    def add_phone(self, phone):
        self.phones.append(phone)
    #Реалізація методу видалення телефону
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    #Реалізація методу редагування телефону
    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
    #Реалізація методу пошуку телефону
    def find_phone(self, phone):
        return phone in self.phones
       
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    #Реалізація методу додавання до data
    def add_record(self, record):
        self.data[record.name.value] = record
    #Реалізація методу пошуку телефону за ім'ям in data
    def find(self, name):
        for record in self.data.values():
            if record.find_phone(name):
                return record.name.value
        return None
    #Реалізація методу видалення з data
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

#if __name__ == "__main__":
    