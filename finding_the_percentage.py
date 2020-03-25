if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for student_name in student_marks:
    if student_name == query_name:
        print('{0:.2f}'.format(sum(student_marks[student_name])/3))
        break
        #for num in student_marks[student_name]:
            #sum
