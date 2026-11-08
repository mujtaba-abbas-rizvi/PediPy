import pytest
from src.person import Person
from src.pedigree import Pedigree

@pytest.fixture 
def emp_ped():
    ped = Pedigree()
    yield ped
    ped.people.clear()

@pytest.fixture
def per():
    muj = Person("Mujtaba","p1","M",False)
    return muj

@pytest.fixture
def p(per):
    ped = Pedigree()
    ped.add_person(per)
    yield ped
    ped.people.clear()
@pytest.fixture
def dup():
    shoa = Person("Shoa","p1","F",False)
    zara = Person("ZARA","p1","F",True)
    return shoa,zara

@pytest.fixture
def full_siblings():
    ped = Pedigree()
    mujtaba = Person("Mujtaba","p1","M",False,"P3","P4")
    shoa = Person("Shoa","p2","F",False,"P3","P4")
    ped.add_person(mujtaba)
    ped.add_person(shoa)
    yield ped, mujtaba, shoa
    ped.people.clear()

@pytest.fixture
def half_siblings():
    ped = Pedigree()
    person1 = Person("mujtaba","p1","M",False,"p4","p5")
    person2 = Person("hasan","p2","F",True,"p4","p3")
    ped.add_person(person1)
    ped.add_person(person2)
    yield ped, person1, person2
    ped.people.clear()
    
@pytest.fixture
def parents():
    ped = Pedigree()
    person1 = Person("mujtaba", "p1", "M", False, "p2", "p3")
    person2 = Person("Raza", "p3", "M", False, )
    ped.add_person(person1)
    ped.add_person(person2)
    yield ped, person1, person2
    ped.people.clear()

@pytest.fixture
def unrelated():
    ped = Pedigree()
    per1 = Person("Mujtaba", "p1","M",False, "p5","p7")
    per2 = Person("lolu","p2","M",True,"p4","p3")
    yield ped, per1,per2
    ped.people.clear()
    
def test_pedigree(p,per):
    assert p.get_person("p1") == per
    assert p.get_person("p99") is None
    
def test_duplicates(emp_ped,dup):
    Zara, Shoa = dup
    emp_ped.add_person(Zara)
    with pytest.raises(ValueError, match="person with p1 already exist"):
         emp_ped.add_person(Shoa)

def test_len(p):
    assert len(p) == 1
    
def test_full_siblings(full_siblings):
    ped, person1, person2 = full_siblings
    assert ped.get_relationship(person1, person2) == "full siblings"
    
    
def test_half_siblings(half_siblings):
        ped, person1,person2 = half_siblings
        assert ped.get_relationship(person1, person2) == "half siblings" 
        
def test_parents(parents):
    ped, person1, person2 = parents
    assert ped.get_relationship(person2,person1) == "parent"
    assert ped.get_relationship(person1,person2) == "child"

def test_unrelated(unrelated):
    ped, p1, p2 = unrelated
    assert ped.get_relationship(p1,p2) == "unrelated"
def test_unknown_parent():
    ped = Pedigree()
    person1 = Person("aditya","p1","F",True,"M1")
    person2 = Person("Narayan","p2","M",False,"M1")
    assert ped.get_relationship(person2,person1) == "siblings"
    ped.people.clear()
def test_diff_m_unk_f():
    ped = Pedigree()
    person1 = Person("aditya","p1","F",True,"M1")
    perosn2 = Person("Narayan","p2","M",False,"M2")
    assert ped.get_relationship(person1,perosn2) == "unrelated"  
    ped.people.clear() 
    
def test_male_mother():
    ped = Pedigree()
    person = Person("A","p1","M",True,"p2","p3")
    mother = Person("B","p2","M",False)
    father = Person("c","p3","M",False)
    ped.add_person(person)
    ped.add_person(mother)
    ped.add_person(father)
    with pytest.raises(ValueError, match="A Male can not be a Mother"):
        ped.validate_pedigree()
    ped.people.clear()

def test_female_father():
    ped = Pedigree()
    person = Person("A","p1","F",True,"M1","p2")
    father = Person("B","p2","F",True)
    mother = Person("C","M1","F",True)
    ped.add_person(person)
    ped.add_person(father)
    ped.add_person(mother)
    with pytest.raises(ValueError, match="A Female can not be a Father"):
        ped.validate_pedigree()
    ped.people.clear() 
    
def test_sex():
    ped = Pedigree()
    child = Person("C","P1","M",False,"P3","P2")
    father = Person("A","P2","M",False)
    mother = Person("B","P3","F",True)
    ped.add_person(child)
    ped.add_person(father)
    ped.add_person(mother)
    assert ped.validate_pedigree() is None

def test_missing_mother():
    ped = Pedigree()
    child = Person("A","p1","M",True,"p99")
    mother = Person("b", "p2", "F",False)
    ped.add_person(child)
    ped.add_person(mother)
    with pytest.raises(ValueError, match="Mother ID doesn't exist"):
        ped.validate_pedigree()
        
def test_missing_father():
    ped = Pedigree()
    child = Person("a","p1","M",True,"p2","p33")
    mother = Person("b", "p2", "F",False)
    father = Person("c", "p3", "F",False)
    ped.add_person(child)
    ped.add_person(mother)
    ped.add_person(father)
    with pytest.raises(ValueError, match="Father ID doesn't exist"):
        ped.validate_pedigree()
    

def test_valid_sex():
    with pytest.raises(ValueError, match="Sex must be M, F or U"):
        Person("A","P1","trans",False)

def test_self_mother():
    with pytest.raises(ValueError, match="A person can not be their own mother"):
        Person("A","P1","M",True,"P1")
def test_self_father():
    with pytest.raises(ValueError, match="A person can not be their own father"):
        Person("a","p1","F",False,"p2","p1")
        
def test_empty_id():
    with pytest.raises(ValueError, match="person ID can not be empty"):
        Person("a","","F",False)
        
def test_grandparent_via_father():
    ped = Pedigree()
    gp = Person("A", "p1","M",False)
    f = Person("B","p2","M",False,None,"p1")
    child = Person("C","p3","M",False,None,"p2")
    ped.add_person(gp)
    ped.add_person(f)
    ped.add_person(child)
    
    assert ped.get_relationship(gp,child) == "grandparent"

def test_gp_via_mother():
    ped =  Pedigree()
    gp = Person("A", "p1","M",False)
    m = Person("B","p2","F",False,None,"p1")
    child = Person("c","p3","M",False,"p2")
    ped.add_person(gp)
    ped.add_person(m)
    ped.add_person(child)
    
    assert ped.get_relationship(gp,child) == "grandparent"
    
def test_grandchild_via_father():
    pedigree = Pedigree()

    grandparent = Person("A", "1", "M", False)
    parent = Person("B", "2", "M", False, father_id="1")
    child = Person("C", "3", "F", False, father_id="2")

    pedigree.add_person(grandparent)
    pedigree.add_person(parent)
    pedigree.add_person(child)

    assert pedigree.get_relationship(child, grandparent) == "grandchild"
    
def test_grandchild_via_mother():
    pedigree = Pedigree()

    grandparent = Person("A", "1", "F", False)
    parent = Person("B", "2", "F", False, mother_id="1")
    child = Person("C", "3", "M", False, mother_id="2")

    pedigree.add_person(grandparent)
    pedigree.add_person(parent)
    pedigree.add_person(child)

    assert pedigree.get_relationship(child, grandparent) == "grandchild"
    
def test_grandparent_missing_intermediate_parent():
    pedigree = Pedigree()

    grandparent = Person("A", "1", "M", False)
    child = Person("C", "3", "F", False, father_id="2")

    pedigree.add_person(grandparent)
    pedigree.add_person(child)

    assert pedigree.get_relationship(grandparent, child) == "unrelated"