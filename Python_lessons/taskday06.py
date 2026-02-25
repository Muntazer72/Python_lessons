# Task:  Write a program to show marks and say  congratulations if marks are above 50 and show the percentage and marks in output also and total marks are 100
#  if the student has less than 50 marks then show You are fail please try again next year

marks = float(input("Enter you marks: "))
percentage = marks/100*100
if marks>50 and percentage>50:
    print(f" Congratulations You are passed!!!\n Your marks are:{marks} and your percentage is: {percentage}")
else:
    print("You are fail please try again next year")