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
            if not person_id:
                raise ValueError("person ID can not be empty")
            self.person_id = person_id
            if sex not in ("M","F","U"):
                raise ValueError("Sex must be M, F or U")
            self.sex = sex
            if affected not in (True,False):
                raise ValueError("Affected must be True/False")
            self.affected = affected
            if person_id == mother_id:
                raise ValueError("A person can not be their own mother")
            self.mother_id = mother_id
            if person_id == father_id:
                raise ValueError("A person can not be their own father")
            self.father_id = father_id
     