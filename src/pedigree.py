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
    
    
    def get_relationship(self,person1,person2):
        if person1.person_id == person2.person_id:
            return "same individual"
        
        if person1.person_id == person2.mother_id or person1.person_id == person2.father_id :
            return "parent" 
        if person2.person_id == person1.mother_id or person2.person_id == person1.father_id :
            return "child"
        if(
          person1.mother_id is not None
          and person1.father_id is not None
          and person2.mother_id is not None
          and person2.father_id is not None  
        ):
            
            if (person1.mother_id == person2.mother_id) and (person1.father_id == person2.father_id):
                return "full siblings"
            if (person1.mother_id == person2.mother_id) or (person1.father_id == person2.father_id):
                return "half siblings"
        if (
            (
                person1.mother_id is not None
            and person2.mother_id is not None
            and person1.mother_id == person2.mother_id
            )
            or (
                person1.father_id is not None
            and person2.father_id is not None
            and person1.father_id == person2.father_id
            )
        ):
            return "siblings"
        father = self.get_person(person2.father_id)
        if father is not None:
            if(father.mother_id == person1.person_id or 
               father.father_id == person1.person_id):
                return "grandparent"
            
        mother = self.get_person(person2.mother_id)
        if mother is not None:
            if(mother.father_id == person1.person_id or
               mother.mother_id == person1.person_id):
                return "grandparent"
        child_father = self.get_person(person1.father_id)
        child_mother = self.get_person(person1.mother_id)
        if child_father is not None:
            if(child_father.father_id == person2.person_id or
               child_father.mother_id == person2.person_id):
                return "grandchild"
        if child_mother is not None:    
            if(child_mother.father_id == person2.person_id or
               child_mother.mother_id == person2.person_id):
                return "grandchild"
            
            
           
          
        return "unrelated"
    
    
    def validate_pedigree(self):
        for person in self.people.values():
            mother = self.get_person(person.mother_id)
            if person.mother_id is not None and mother is None:
                raise ValueError("Mother ID doesn't exist")
            father = self.get_person(person.father_id)
            if person.father_id is not None and father is None:
                raise ValueError("Father ID doesn't exist")
            if mother is not None and mother.sex == "M":
                raise ValueError("A Male can not be a Mother")
            if father is not None and father.sex == "F":
                raise ValueError("A Female can not be a Father")
            