from main import Person

Sonny  = Person("Sonny", 'sonny@hotmail.com', '483-485-4948')
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')

# print(Sonny.friends)

# Jordan.friends.append(Sonny)
# Sonny.friends.append(Jordan)

# print(len(Jordan.friends))

Jordan.add_friend(Sonny)
Jordan.num_friends()
Jordan.print_contact_info()

Sonny.greet(Jordan)
Sonny.greeting_count

Jordan.greet(Sonny)
Jordan.greeting_count