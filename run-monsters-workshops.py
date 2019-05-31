# from<filename> import (function, classes or *)
from workshops_class import *
from monster_class import *

# create 1 workshop
work_shop1 = Workshop('Creating Chaos for better fear')

# create 3 monsters
sully = Monster('Sully', 22, 9999)
omenen = Monster('Omenen', 665, 665)
karen = Monster('Karen', 44, 1300)

# Append our monsters to our workshop
work_shop1.enroll_monster_student(sully)
work_shop1.enroll_monster_student(omenen)
work_shop1.enroll_monster_student(karen)

# variable to hold our attendees_list of our workshop instance
list_enrolled = work_shop1.attendees_list

for monster in list_enrolled:
    print(monster, monster.name)
    print(monster.name, 'has a scary rating of', monster.scary_rating)

