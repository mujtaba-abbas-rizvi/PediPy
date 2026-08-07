class Person:
    def __init__(
        self,name,
        person_id,
        sex,
        affected,
        mother_id=None,
        father_id=None
        ):
            self.name = name
            self.person_id = person_id
            self.sex = sex
            self.affected = affected
            self.mother_id = mother_id
            self.father_id = father_id
