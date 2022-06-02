import csv
from classes.Person import Person

class Staff(Person):
    
    def all_staff():
        all_staf = []
        with open('/Users/lamberto/codeExercises/Day8/oop-school-interface-i/data/staff.csv') as f: 
            reader = csv.DictReader(f)
            
            for row in reader:
                all_staf.append(row)
    
            return(all_staf)