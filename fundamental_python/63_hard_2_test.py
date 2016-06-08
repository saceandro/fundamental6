#!/usr/bin/env python

class Person:
    def __init__(self, family_name, given_name, age):
        self.family_name = family_name
        self.given_name = given_name
        self.age = age
    
    def __lt__(self, other):
        if self.family_name != other.family_name:
            return self.family_name < other.family_name
        if self.age != other.age:
            return self.age < other.age
        return self.given_name < other.given_name

# l = []
# l.append(Person("Sato", "Taro", 18))
# l.append(Person("Sato", "Hanako", 17))
# l.append(Person("Sato", "Aiko", 20))
# l.append(Person("Tanaka", "Hirofumi", 30))
# l.append(Person("Tanaka", "Masako", 28))
# l.append(Person("Aizawa", "Hanako", 9))
# l.sort()
# for i in l:
#     print "%s %s (%d)" % (i.family_name, i.given_name, i.age)
