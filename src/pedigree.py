from .person import Person


class Pedigree:
    def __init__(self):
        self.people = {}
        
        
    def add_person(self, person: Person):
        if person.person_id in self.people:
            raise ValueError(f"person with {person.person_id} already exists")
        self.people[person.person_id] = person
        
        
    def get_person(self,person_id: str):
        return self.people.get(person_id)
    
    def __len__(self):
        return len(self.people)