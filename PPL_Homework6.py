import re
#For this project, we need to wrtie a python program to output an HTML file titled "output.html" that describes a table. This table should
#list studetn records, with one student per row. Each record will contain a last name, first name, ID number, & letter grade. This table will be sorted
#by Last name, then first name and ID

#Important notes
# A tie can always be broken by the eagerness of a students
#Each ID is a 9-digit integer & no duplicate IDs exist
#The only module that should be importes id re (regular expression)

#I think we can start by making a student class with a variable for each of the values
class Student:
    def __init__(self, firstName, lastName, grade, ID, eagerness):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
        self.ID = ID
        self.eagerness = eagerness
        self.letterGrade = "Unassigned"
    
    def __repr__(self):
        return f"{self.firstName} {self.lastName} {self.grade} {self.ID} {self.eagerness}"
    #All this method does is print out each student class for the sake of ensuring the records are stored correctly

    def __reprwithGrades__(self):
        return f"{self.firstName} {self.lastName} {self.grade} {self.ID} {self.eagerness} {self.letterGrade}"

    def _printGrades_(self):
        return f"{self.letterGrade}"

    @classmethod
    def assign_letter_grades(cls, student_list):
        """Assign letter grades according to the specified rules"""
        if not student_list:
            return
            
        # Sort by grade (descending) and eagerness (E before L)
        sorted_students = sorted(student_list,
                               key=lambda s: (-int(s.grade), s.eagerness))
        
        n = len(sorted_students)
        a_cutoff = n // 3
        b_cutoff = 2 * (n // 3)
        f_cutoff = n - (n // 10)  # Bottom n/10
        
        for i, student in enumerate(sorted_students, start=1):
            if i <= a_cutoff:
                student.letterGrade = "A"
            elif i <= b_cutoff:
                student.letterGrade = "B"
            elif i > f_cutoff:
                student.letterGrade = "F"
            else:
                student.letterGrade = "C" if student.eagerness == "E" else "D"
#Loop system needs reworking


studentList = [] #Will be filled with Student objects once the records are created

#We have an initial student class. From here we can probably start reading in the file & manipulating the strings to obtain the data we need
with open("input.txt", "r") as file:
    #reads the whole file
    content = file.read()
#We now have the entire input.txt in the program. From here we can go line by line & read in data to fill out student records

#We can start by getting a list of all the IDs & assigning them to new student classes. Thankfully while the format of the file is junk,
#The information for each student is in a specific style; that being
        #   ID - FIRSTNAME - LASTNAME - GRADE - EAGERNESS - LOCATION(OPTIONAL)

    #What if I did a split() function?
list = re.split("\s",content)
#So I think I just made this really easy with this...
#Since we know the format of the file, we could probably loop thrugh & create our list of students from there

#To figure out the amount of objects we need to create, we can use the findall function in re to find how many ID numbers exist in content, due to the ID
#numbers having several static characteristics

#Specific characteristics to utilize - The entire thing contains integer characters, and is exactly 9 characters long
idList = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",content)
#List that finds all the IDs in the string

gradeList = re.findall(r'(?<=\s)\d{2}(?=\s)', content) 
#This finds all values which are two digit numbers surrounded by whitespace, AKA the grades in the content string for each student

#findall(Values that are either E or L and are surrounded by spaces)
eagernessList = re.findall(r'(?<=\s)[a-zA-Z]{1}(?=\s)', content)
#Line above parses through content to find all of the Eagerness tags

#All that's left to do at this point is acquire the names. Luckily, since we know the format of each record, we can do some trickery
#using re.sub to manipulate already acquired data to create a kind of box around the content we need, while ignoring the rest.
trimmedContent = re.sub("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", "START",content) 
#This line above replaces all ID numbers with the string START
superTrimmedContent = re.sub(r'(?<=\s)\d{2}(?=\s)', "END",trimmedContent)
#This line replaces all grade values with the string END

#With the content in the string manipulated, we can again utilize findall to search for subtrings that start with START and end with END
#This gives us a rough list of names - rough in the sense that the values need trimming to remove whitespace or newline characters
# Find all matches (including across newlines)
matches = re.findall(r'START(.*?)END', superTrimmedContent, flags=re.DOTALL)

# Clean each match: 
# 1. Replace any internal whitespace (including newlines) with single space
# 2. Strip surrounding whitespace
clean_matches = [' '.join(match.split()) for match in matches]
#I AM A GENIUS AMONGST MEN WHO HAS THOUGHT OF THIS BEFORE

firstNames = []
lastNames = []

for full_name in clean_matches:
    parts = full_name.split()

    firstNames.append(parts[0])
    lastNames.append(parts[1])



#from here we can create x amount of student objects, where x is the number of ids found / the length of idList & assign everything directly
for i in range(len(idList)):
    studentList.append(Student(firstName=firstNames[i], lastName=lastNames[i], grade=gradeList[i], ID= idList[i], eagerness=eagernessList[i]))

for student in studentList:
    print(Student.__repr__(student))

Student.assign_letter_grades(studentList)

for student in studentList:
    print(Student._printGrades_(student))

for student in studentList:
    print(Student.__reprwithGrades__(student))

#We know have every student record created and ready for the rest of the operations

#Next, we need to make a method for determining letter grades. We can accomplish this by referring to the rules for the grading system & applying them
#to the list of students which are sorted by grades in decending order.