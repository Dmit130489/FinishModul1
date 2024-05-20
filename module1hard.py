grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_mark_A = sum(grades[0]) / len(grades[0])
average_mark_B = sum(grades[1]) / len(grades[1])
average_mark_J = sum(grades[2]) / len(grades[2])
average_mark_K = sum(grades[3]) / len(grades[3])
average_mark_S = sum(grades[4]) / len(grades[4])
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
average_mark = {}
average_mark[students[0]] = average_mark_J
average_mark[students[1]] = average_mark_B
average_mark[students[2]] = average_mark_S
average_mark[students[3]] = average_mark_K
average_mark[students[4]] = average_mark_A
print(average_mark)