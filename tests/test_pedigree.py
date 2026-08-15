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