from monster_class import *

# -AS A user I WANT to create a monster from Monster()
monster_example = Monster()

# Behaviours of monster (methods):
print("A monster should be able to sleep -> respond back with something including 'zzzz'")
print(monster_example.sleep() == 'zzzz')
print('//////////////////////////////')

# - A monster should be able to eat -> respond back with something including 'nom nom'
print("A monster should be able to eat -> respond back with something including 'nom nom'")
print(monster_example.sleep() == 'nom nom')
print('//////////////////////////////')

# - A monster should be able to scare_attack -> respond back with something including 'RAAAAHHH'
print("A monster should be able to scare_attack -> respond back with something including 'RAAAAHHH'")
print(monster_example.scare_attack() == 'RAAAAHHH')
print('//////////////////////////////')

# - Should be able to add a skill to list of skills
print("Should be able to add a skill to list of skills")
print(monster_example.add_skill('stealth') == 'stealth' in monster_example.skills)
print('//////////////////////////////')

# Monster should be able to hide --> should return 'You can't seeee meee, go back to sleeeep


# Looks of a monster (Attributes):

# - Should have a name (string)
print("Monster should have a name (string)")
print(type(monster_example.name) == type(""))
print('//////////////////////////////')

#Diff names
print("When we create a monster with a name 'Ringo', we get a monster with that name as an attribute")
print(monster_ringo.name == 'Ringo')
print('//////////////////////////////')

# - Should have a list of skills
print("Should have a list of skills")
print(type(monster_example.skills) == list)

# A monster should have an age as an integer

# When we create a monster with age 3000 years old, we should get a monster with that age


