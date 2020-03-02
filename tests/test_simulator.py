import unittest

from buzz import simulator

def test_simulator_key():
    l = ('device', 'zombie', 'simm')
    word = simulator.sample(l)
    assert word in l

def test_simulator_multiple_keys():
    l = ('IOT', 'sensor', 'hybrid')
    words = simulator.sample(l, 2)
    assert len(words) == 2
    assert words[0] in l
    assert words[1] in l
    assert words[0] is not words[1]

def test_simulator_sentence():
    phrase = simulator.generate_simulation()
    assert len(phrase.split()) >= 5
