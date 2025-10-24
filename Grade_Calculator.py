counter = 1
MAX_VALUE = 1
score = 0
total_usr_score = 0



print("Grade Calculator \n ----------------")

usr_assignments = input("How many assignments are in this class? (In Whole Numbers, no decimals!) ")

while True:
    if usr_assignments.isdigit():
        assignments = int(usr_assignments)
        total_assignments = assignments + MAX_VALUE
        
        while counter in range(total_assignments):
            score = float(input(f"What is the score for assignment #{counter}? (Can do both Whole Numbers/Decimal) "))
            
            if score < 0 or score > 100:
                print("Please input a valid grade between 0 - 100!")
            else:
                total_usr_score += score
                counter += 1     

        total_score = total_usr_score/assignments

        print(f"The final score is {total_score:.2f}%")
        break

    else:
        print("Please input a valid Whole Number greater than 0, no Decimals!")
        break