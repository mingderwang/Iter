student_grades = [57, 74, 49, 0, 87, 66, 89]
print(type(student_grades))
print('-------- use for loop on a list')
for g in student_grades:
  print(g)
  if g >= 52: 
    print('This student passed.')
  else:
    print('This student failed.')

print('Program complete')
print()
print('-------- use iter in a while loop ---')
sg = iter(student_grades)
print(type(sg))
while True:
  try:
    g = next(sg)
    print(g)
    if g >= 52: 
      print('This student passed.')
    else:
      print('This student failed.')
  except StopIteration:
    print('Program complete')
    break

print()
print('-------- try filter -------')
sg = iter(student_grades)
result = filter(lambda x: x >= 52, sg) 
print(list(result))
print('These students are passed.')