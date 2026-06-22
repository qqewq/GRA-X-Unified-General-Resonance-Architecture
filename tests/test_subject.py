from gra_subject.subject_swap import SubjectSwapper
from gra_subject.identity import Identity

def test_swap():
    a = Identity("A")
    b = Identity("B")
    s = SubjectSwapper(a)
    s.swap(b)
    assert s.current.name == "B"
