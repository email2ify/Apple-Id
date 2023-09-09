#for i in range(1,5):
#   for j in range(1,7):
#      print(f'({i},{j})')


students = {
    'Ben' : 'New York',
    'Bob' : 'Los Agenles',
    'Mark' : 'Lagos'
}

students['Ben']

for student in students:
    print(f'{student} is in {students[student]} America')