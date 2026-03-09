''''Extra credits to substitute a quiz grade:
modify this code so number of quizzes is unknown
if you enter a value that is == 999 then you stop asking for a new grade
you need to validate the quiz grade to make sure it is between 0 & 10'''

sum = 0
count = 10  #initializ (count)

while count > 0: #test
    q = int(input("Please enter a grade: "))    
    while q < 0 or q > 10:
        q = int(input("Wrong! Please enter a grade: "))
    #q is a valid value
    sum += q
    count -= 1
#Calculate the average
avg = sum / 10
print(f"Average = {avg}")
