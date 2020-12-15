class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends

    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')

    def print_contact_info(self):
        print(self.name, self.email, self.phone)
