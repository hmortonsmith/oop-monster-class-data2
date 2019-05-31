# we want to create workshops of specific scary skills
# the workshop should have a list to keep Monster objects that are attending


class Workshop:

    def __init__(self, topic, location='Hell'):
        self.attendees_list = []
        self.teacher = ''
        self.location = location
        self.topic = topic

    # self is instance of object

    def set_teacher(self, teacher):
        self.teacher = teacher
        print('[robotic voice] your teacher has been set')
    # setter

    def enroll_monster_student(self, monster):
        self.attendees_list.append(monster)
        print('[robotic voice] your student has been enrolled')
        # if self.attendees_list.append(monster):
        #     print('[robotic voice] your student has been enrolled')
        # else:
        #     print('error')
        