class Monster:

    # define attributes
    def __init__(self, name = '', age = 0):
        self.skills = []
        self.name = name
        self.age = int(age)
        
    # define methods
    def sleep(self):
        return 'zzzz'

    def eat(self):
        return 'nom nom'

    def scare_attack(self):
        return 'RAAAAHHH'

    def list_skills(self):
        return skills()
    
    def hide(self):
        return "You can't seeee meee, go back to sleeeep"
    
    def add_skill(self, skills):
        self.skills.append(skills)
    
