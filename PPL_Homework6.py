import re

#####   Edward Wages - Homework 6 - Python Project: A text lsit to an HTML Table    #####


#For this project, we need to wrtie a python program to output an HTML file titled "output.html" that describes a table. This table should
#list studetn records, with one student per row. Each record will contain a last name, first name, ID number, & letter grade. This table will be sorted
#by Last name, then first name and ID

#Important notes
# A tie can always be broken by the eagerness of a students
#Each ID is a 9-digit integer & no duplicate IDs exist
#The only module that should be importes id re (regular expression)

class Student: #We'll have a student class which will store each variable field once we've acquired them
    def __init__(self, firstName, lastName, grade, ID, eagerness):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = int(grade)
        self.ID = ID
        self.eagerness = eagerness
        self.letterGrade = "Unassigned"

    def __repr__(self):
        return f"{self.firstName} {self.lastName} {self.grade} {self.ID} {self.eagerness}"
    #All this method does is print out each student class for the sake of ensuring the records are stored correctly

    def __reprwithGrades__(self):
        return f"{self.firstName} {self.lastName} {self.grade} {self.ID} {self.eagerness} {self.letterGrade}"
    #Exact same thing was repr but with grades - can be ignored, was just used to check that variables are stored correctly

    def sort_students_final(student_list):
        return sorted(student_list, key=lambda x: (x.lastName, x.firstName, x.ID))
    #Method which does the final sorting of the list according to project specifications

    @classmethod    #This method wouldn't work without specifying as a class method, don't really understand why but it works :)
    def assign_letter_grades(cls, student_list):
        if len(student_list) < 7: #The project specifies we should not be working with a class of less than 7 students
            raise ValueError("Class must have at least 7 students")
            
        # Sort by grade (descending) and eagerness (E comes first)
        sorted_students = sorted(student_list, 
                               key=lambda x: (-x.grade, 0 if x.eagerness == 'E' else 1))
        
        n = len(sorted_students) #Preparing variables ahead of time for the grade range
        a_cutoff = n // 3
        b_cutoff = 2 * (n // 3)
        f_cutoff = n - ((n + 9) // 10) 
        
        # Assign grades
        for i, student in enumerate(sorted_students):
            if i < a_cutoff:
                student.letterGrade = "A"
            elif i < b_cutoff:
                student.letterGrade = "B"
            elif i >= f_cutoff:
                student.letterGrade = "F"
            else:
                student.letterGrade = "C" if student.eagerness == "E" else "D"


studentList = [] #Will be filled with Student objects once the records are created

#We have an initial student class. From here we can  start reading in the file & manipulating the strings to obtain the data we need
with open("input.txt", "r") as file:
    #reads the whole file
    content = file.read()
#We now have the entire input.txt in the program. From here we can go line by line & read in data to fill out student records

#We can start by getting a list of all the IDs & assigning them to new student classes. Thankfully while the format of the file is junk,
#The information for each student is in a specific style; that being
        #   ID - FIRSTNAME - LASTNAME - GRADE - EAGERNESS - LOCATION(OPTIONAL)

#To figure out the amount of objects we need to create, we can use the findall function in re to find how many ID numbers exist in content, due to the ID
#numbers having several static characteristics we can take advantage of

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

firstNames = []
#list of each student's first name
lastNames = []
#Self explanatory

#Loop to assign the names
for full_name in clean_matches:
    parts = full_name.split()

    firstNames.append(parts[0])
    lastNames.append(parts[1])

#from here we can create x amount of student objects, where x is the number of ids found / the length of idList & assign everything directly.
#Technically this could be accomplished with any of the lists, but I went with IDlist since that's the once I figured out how to do first
for i in range(len(idList)):
    studentList.append(Student(firstName=firstNames[i], lastName=lastNames[i], grade=gradeList[i], ID= idList[i], eagerness=eagernessList[i]))

#Next we assign the letter grades of the students
Student.assign_letter_grades(studentList)

sorted_Records = Student.sort_students_final(studentList)
#Sorts the student list as specified in the homework document (Last name, first name, ID)

#Now we'll start writing our findings to the HTML file

with open("output.html", "w") as file:
    # Write HTML header and table structure
    file.write("""<!DOCTYPE html>
<html>
<head>
    <title>Student Grades</title> 
    <style>
        table 
        {
            border-collapse: collapse;
            width: 100%;
        }
        th, td 
        {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th 
        {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Student Grades</h1>
    <table>
        <tr>
            <th>Last Name</th>
            <th>First Name</th>
            <th>ID</th>
            <th>Letter Grade</th>
        </tr>
""")

    # Write each student's data as a table row
    for student in sorted_Records:
        file.write(f"""        <tr>
            <td>{student.ID}</td>
            <td>{student.firstName}</td>
            <td>{student.lastName}</td>
            <td>{student.letterGrade}</td>
        </tr>
""")

    # Close the HTML tags
    file.write("""    </table>
</body>
</html>""")
    
#That's the whole thing! Some edge cases which I have attempted to cover for:
    #Class being less than 7 students
    #Students with similar names will be sorted by ID
    #Don't need to worry too much about similar grades since the project specifies that ties will always be broken by eagerness
#Have a good day!