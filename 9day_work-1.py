student_scores = {}
end = True

while end:
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    
    
    student_scores[name] = marks

    
    for key in student_scores:
        value = student_scores[key]
        print(f"{key}: {value}")

   
    exitt = input("Do you want to exit? (yes/no): ")
    if exitt.lower() == 'yes':
        end = False
        print("You exited.")
