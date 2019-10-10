class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3


def test_tuberculosis_instantiation():
    virus = Virus("Tuberculosis", 0.67, 0.55)
    assert virus.name == "Tuberculosis"
    assert virus.repro_rate == 0.67
    assert virus.mortality_rate == 0.55


def test_rotavirus_instantiation():
    virus = Virus("Rotavirus", 1.6, 0)
    assert virus.name == "Rotavirus"
    assert virus.repro_rate == 1.6
    assert virus.mortality_rate == 0


def test_whooping_cough_instantiation():
    virus = Virus("Whooping Cough", 1.45, 0.05)
    assert virus.name == "Whooping Cough"
    assert virus.repro_rate == 1.45
    assert virus.mortality_rate == 0.05
