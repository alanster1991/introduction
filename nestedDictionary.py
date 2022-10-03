from this import s
from turtle import st


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Jordan"
print(students)
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print(students[0])
def iterateDictionary(students):
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    for index in range(len(students)):
        print(f"first_name - {students[index]['first_name']}, last_name - {students[index]['last_name']} ")
    return students
iterateDictionary(students)

def iterateDictionary2(key, list):
    for index in range(len(list)):
        print(students[index][key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    count = 0
    for key in dict:
        count = len(dict[key])
        print(f" {count} {key.upper()}")
        for index in range(len(dict[key])):
            print(dict[key][index])

printInfo(dojo)