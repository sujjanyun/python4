class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')
        self.greeting_count += 1

    def print_contact_info(self):
        print(self.name, self.email, self.phone, self.friends)

    def add_friend(self, friend):
        print(f'My name is {self.name} and my friend is {friend.name}')
        self.friends.append(friend.name)

    def num_friends(self):
        print(f"And I have {len(self.friends)} friend.")
    
    def greeting_count(self):
        print({self.greeting_count})