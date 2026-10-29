from time import sleep

Targets = ['Pentagon',
           'Amazon AWS',
           'DoD',
           'DoW',
           'Strategic Defense Initiative',
           'Apple',
           'General Dynamics',
           'Lockheed Martin',
           'East Seabase Missile Port']

for i in range(len(Targets)):
    target = Targets[i%len(Targets)]
    print("hacking ",target)
    sleep(1.2)