"""
Testing function calls
"""
from functions import semMarks, hobbies, cities, progLangs, domains


def test_sem_marks():
    assert semMarks.sem_marks(7) == True


def test_hobbies():
    assert hobbies.hobbies(5) == True


def test_cities():
    assert cities.cities(4) == True


def test_prog_lang():
    assert progLangs.programming_languages(8) == True


def test_domains():
    assert domains.domains(8) == True
