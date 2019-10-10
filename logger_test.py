import unittest
import logger
import person
import virus
import os

class logger_Tests(unittest.TestCase):
    '''This tests all possible reasons for the logger being called. I'm unsure
    if I should be testing for edge cases here and I didn't because all of the
    values passed in by the simulation will not contain edge cases.'''
    def test_create_logger(self):
        _logger = logger.Logger('HI')
        assert _logger.file_name == 'HI'
        assert _logger.file_name != 'hello'
        assert _logger.file_name == _logger.file_name
    def test_write_metadata(self):
        _logger = logger.Logger('what.txt')
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n'''
        file.close()
        os.remove("what.txt")
    def test_log_interaction_fail_to_infect(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _person2 = person.Person(2, False)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_interaction(_person, _person2)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} failed to infect {2} \n'''
        file.close()
        os.remove("what.txt")
    def test_log_interaction_succed_to_infect(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _person2 = person.Person(2, False)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_interaction(_person, _person2, None, None, True)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} did infect {2} \n'''
        file.close()
        os.remove("what.txt")
    def test_log_interaction_fail_to_infect_sick(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _person2 = person.Person(2, False)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_interaction(_person, _person2, True, None, None)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} did not infect already sick person {2} \n'''
        file.close()
        os.remove("what.txt")
    def test_log_interaction_fail_to_infect_vacc(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _person2 = person.Person(2, False)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_interaction(_person, _person2, None, True, None)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} did not infect vaccinated person {2} \n'''
        file.close()
        os.remove("what.txt")
    def test_log_infection_survival_true(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_infection_survival(_person, True)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} died from infection \n'''
        file.close()
        os.remove("what.txt")
    def test_log_infection_survival_false(self):
        _logger = logger.Logger('what.txt')
        _virus = virus.Virus("Tuberculosis", 0.67, 0.55)
        _person = person.Person(1, False, _virus)
        _logger.write_metadata(100, 0.5, 'Virus', 0.5, 0.5)
        _logger.log_infection_survival(_person, False)
        file = open(_logger.file_name, 'r')
        assert file.read() == f'''{str(100)}\t{str(0.5)}\t{'Virus'}\t{str(0.5)}\t{str(0.5)}\n{1} became immune to the infection \n'''
        file.close()
        os.remove("what.txt")


if __name__ == '__main__':
    unittest.main()
