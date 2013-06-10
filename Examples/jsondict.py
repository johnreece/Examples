# JSON and complex dictionary of dictionaries of dictionaries data structures
#
#     The JSON structure
#
import json

staff = { "employees" : [
            { "person" : 
                    [ {"first" : "Joseph", "last" : "Blow" } ]
            },
            {     "person" :
                    [ {"first" : "Joe", "last" : "Doakes" } ]
            },
            {  "person" :
                    [  {"first" : "Jane", "last" : "Doe" } ]
            }
                    ] 
        }

# The Dictionaries of dictionaries (of dictionaries) structure

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):
#
#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# a JSON structure is a dictionary containing a list containing dictionaries, each containing a list
# containing dictionaries, each containing a list...so alternate string and integer indices.
s =  staff["employees"][1]['person'][0]["last"]
print s, "\n"
for p in staff["employees"]:
    print p["person"][0]["first"], " ", p["person"][0]["last"]



# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary. For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# [Double Gold Star] Define a procedure, involved(courses, person), that takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester (the courses in the list 
# can be in any order).

def involved(courses, person):
        output = {}
        for hexamester in courses:
            for course in courses[hexamester]:
                for field in courses[hexamester][course]:
                    if courses[hexamester][course][field] == person:
                        if hexamester in output:
                            output[hexamester].append(course)
                        else:       # No entry yet so add
                            output[hexamester] = [course]
        return output
            
    



# For example:

print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

#print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

#print involved(courses,'Peter')
#>>> {}

#print involved(courses,'Robotic')
#>>> {}

#print involved(courses, '')
#>>> {}
