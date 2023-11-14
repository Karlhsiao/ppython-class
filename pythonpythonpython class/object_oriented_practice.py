import datetime

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return "I am " + str(self.name)

    def get_age(self):
        today = datetime.date.today()
        year = today.year

        print(year - self.birth_year)


class student(Person):
    def __init__(self, sid, name, birth_year):
        self.sid = sid
        self.lessons = []
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return "No." + str(self.sid) + " " + str(self.name)
    
    def add_lesson(self, lesson):
        self.lessons.append(lesson)

may = Person("May", 2009)

print(may)
print(may.get_age())

may = student(1, "May", 2009)
print(may)
print(may.get_age())

may.add_lesson("Math")
may.add_lesson("English")
may.add_lesson("Art")
print(may.lessons)
