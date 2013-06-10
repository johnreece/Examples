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


for record in staff['employees']:
    print record['person'][0]['first']," ",record['person'][0]['last']

print courses.keys()
for month in courses:
    print month 
    