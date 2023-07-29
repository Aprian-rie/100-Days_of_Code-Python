# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(" ")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
No_of_students = 0
for height in student_heights:
  sum += height
for student in student_heights:
  No_of_students += 1
average = round(sum / No_of_students, 2)
print(average)
