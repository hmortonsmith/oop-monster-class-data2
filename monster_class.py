class Monster:

    # define attributes
    def __init__(self, name='', age=0, rating=0,):
        self.skills = []
        self.name = name
        self.national_insurance = ''
        self.age = int(age)
        self.scary_rating = rating
        
        
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
        
