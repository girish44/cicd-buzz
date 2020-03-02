from __future__ import print_function
import random

simz = ('simulator ', 'hybrid ', 'IOT ', 'real-world ', 'device ', 'zombie ')
sensors = ('temperature exceeded limit', 'CO alarm triggered', 'milk needs replenishing', 'window broken')
ips = ('10.15.20.25', '12.17.166.23', '15.22.199.111', '27.177.12.55')

def sample(l, n = 1):
    ''' Generate a sample string for simulators'''
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_simulation():
    '''Make up a simulator response to display'''
    sim_terms = sample(simz,2)
    print ("Simm terms ==", sim_terms)
    phrase = ' '.join([ sim_terms[0], sim_terms[1], "with IP address of ", sample(ips), " reported ", sample(sensors)])
    return phrase.title()

if __name__ == "__main__":
    print(generate_simulation())
