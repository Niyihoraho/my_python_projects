student_scores = {}
end = True

while end:
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    
    if 91 <= marks <= 100:    
        student_scores[name] = "Outstanding"
    elif 81 <= marks <= 90:
        student_scores[name] = "Exceeds Expectation"
    elif 71 <= marks <= 80:
        student_scores[name] = "Acceptable"
    else:
        student_scores[name] = "Fail"
    
    exitt = input("Do you want to exit? (yes/no): ")
    if exitt.lower() == 'yes':
        end = False
print(student_scores)

       
        
        