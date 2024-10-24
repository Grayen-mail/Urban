grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_dict = {sorted(students)[num]: sum(grades[num])/len(grades[num]) for num in range(len(students))}

print(students)
print(students_dict)

#Second variant
student_list = sorted(students)
print(dict(zip(student_list, [sum(grade)/len(grade) for grade in grades])))

#print(list(map(lambda grade: sum(grade)/len(grade),grades)))