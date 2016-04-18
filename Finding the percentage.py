
N = raw_input("insert num: ")
dict_line = {}
for line in range(int(N)):
    insert_line = str(raw_input("insert line: "))
    insert_line = insert_line.split()
    student_name = insert_line[0]
    student_score = insert_line[-3:]
    dict_line[student_name] = student_score

check_student_average = raw_input("insert student name for average check: ")
if check_student_average in dict_line:
    score = dict_line[check_student_average]
    average = 0
    for a in score:
        average += float(a)
    average = average / len(score)
    print("%.2f" % average)
    
    
    
    
