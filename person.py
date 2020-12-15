#WORKING WITH EXISTING CLASS

# Given the following Person class:
from main import Person

#Write code to:
# INSTANCE
#Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
Sonny  = Person("Sonny", 'sonny@hotmail.com', '483-485-4948')

#Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable jordan.
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')

#Have sonny greet jordan using the greet method.
Sonny.greet(Jordan)

#Have jordan greet sonny using the greet method.
Jordan.greet(Sonny)

#Write a print statement to print the contact info (email and phone) of Sonny.
print("Sonny")
print(Sonny.email)
print(Sonny.phone)

#Write another print statement to print the contact info of Jordan.
print(Jordan.name)
print(Jordan.email)
print(Jordan.phone)