
def get_name():
    prompt = "What is your name?: "
    while True:
        name = input(prompt).strip()
        if len(name) == 0:
            prompt = "Please enter your name: "
            continue
        return name
def get_age():
    prompt = "How old are you?: "
    while True:
        age = input(prompt).strip()
        if len(age) == 0:
            prompt = "Please enter your age: "
            continue
        try:
            age = int(age)
            
            if age < 0:
                prompt = "Age cannot be negative. Please enter your age: "
                continue
            return age
        except:
            prompt = "Please enter numbers only:"

def get_height():
    prompt = "What's your height?: "
    while True:
        height = input(prompt).strip()
        if len(height) == 0:
            prompt = "Please enter your height: "
            continue
        try:
            height = float(height)
            
            if height < 0:
                prompt = "Height cannot be negative. Please enter your height: "
                continue
            return height
        except:
            prompt = "Please enter numbers only:"

def get_grade():
    prompt = "What grade are you in?: "
    while True:
        grade = input(prompt).strip()
        if len(grade) == 0:
            prompt = "Please enter your grade: "
            continue
        try:
            grade = int(grade)
            
            if grade < 1 or grade > 13:
                prompt = "Grade must be between 1 and 13. Please enter your grade: "
                continue
            return grade
        except:
            prompt = "Please enter numbers only:"


def age_check(age):
    if age >= 15:
        return True
    else:
        return False
def height_check(height, sport):
    if sport == "basketball":
        if height >= 1.7:
            return True
        else:
            return False
    if sport == "football":
        if height >= 1.6:
            return True
        else:
            return False
    if sport == "volleyball":
        if height >= 1.75:
            return True
        else:
            return False
         
def grade_check(grade):
    if grade == 10 or grade == 11:
        return True
    else:
        return False
    
    

running = True
while running:
    print()
    print()
    print("Welcome to the sports competition registration!")
    print("We have 3 sports competitions available: basketball, football and volleyball.")
    print()
    selected_sport = input("Which sport competition do you want to participate in?: ").lower() 

    while not selected_sport:
        selected_sport = input("Which sport competition do you want to participate in?: ").lower() 
    while selected_sport != "basketball" and selected_sport != "football" and selected_sport != "volleyball":
        selected_sport = input("Sorry, we don't have that sport competition available, please choose one of the three we have: ").lower() 

    if selected_sport == "basketball":
        print()
        print()
        print("To take part in this basketball competition you need to meet all the following requirements:")
        print("   - You need to be at least 15 years old")
        print("   - You need to be at least 1.7m tall")
        print("   - You need to be in either 10th or 11th grade")
        print()
        print()
        student_name = get_name()
        student_age = get_age()
        student_height = get_height()
        student_grade = get_grade()
        print()
        print()
        if age_check(student_age) and height_check(student_height, selected_sport) and grade_check(student_grade):
            print(student_name + ", you passed all the requirements, so you can participate!")
        else:
            if not age_check(student_age):
                print("You are not old enough to participate ")
            if not height_check(student_height, selected_sport):
                print("You are not tall enough to participate ")
            if not grade_check(student_grade):
                print("You are not in the correct grade to participate ")


    if selected_sport == "football":
        print()
        print()
        print("To take part in this football competition you need to meet all the following requirements:")
        print("   - You need to be at least 15 years old")
        print("   - You need to be at least 1.6m tall")
        print("   - You need to be in either 10th or 11th grade")
        print()
        print()
        student_name = get_name()
        student_age = get_age()
        student_height = get_height()
        student_grade = get_grade()
        print()
        print()
        if age_check(student_age) and height_check(student_height, selected_sport) and grade_check(student_grade):
            print(student_name + ", you passed all the requirements, so you can participate!")
        else:
            if not age_check(student_age):
                print("You are not old enough to participate ")
            if not height_check(student_height, selected_sport):
                print("You are not tall enough to participate ")
            if not grade_check(student_grade):
                print("You are not in the correct grade to participate ")

    if selected_sport == "volleyball":
        print()
        print()
        print("To take part in this volleyball competition you need to meet all the following requirements:")
        print("   - You need to be at least 15 years old")
        print("   - You need to be at least 1.75m tall")
        print("   - You need to be in either 10th or 11th grade")
        print()
        print()
        student_name = get_name()
        student_age = get_age()
        student_height = get_height()
        student_grade = get_grade()
        print()
        print()
        if age_check(student_age) and height_check(student_height, selected_sport) and grade_check(student_grade):
            print(student_name + ", you passed all the requirements, so you can participate!")
        else:
            if not age_check(student_age):
                print("You are not old enough to participate ")
            if not height_check(student_height, selected_sport):
                print("You are not tall enough to participate ")
            if not grade_check(student_grade):
                print("You are not in the correct grade to participate ")
            
    register_again = input("Would you like to register for another sport competition?: ").strip().lower()
    if register_again == "no":
        running = False
        print("Thank you for your time, have a nice day!")







    
