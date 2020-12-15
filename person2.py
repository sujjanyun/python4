from main import Person

Sonny  = Person("Sonny", 'sonny@hotmail.com', '483-485-4948', '')
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456', '')

Jordan.friends.append(Sonny)
Sonny.friends.append(Jordan)