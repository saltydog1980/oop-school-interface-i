import csv
from classes.Person import Person

class Student(Person):

    def all_students():
        all_studs = []
        with open('/Users/lamberto/codeExercises/Day8/oop-school-interface-i/data/students.csv') as f: 
            reader = csv.DictReader(f)
            
            for row in reader:
                all_studs.append(row)
    
            return(all_studs)
            
