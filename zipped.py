width, height = map(int, input().split())
subject_notes = list()
for subject_index in range(height):
    subject_notes.append(list(map(float, input().split())))

students = list(zip(*subject_notes))
for student in students:
    print(sum(student)/len(student))
    
