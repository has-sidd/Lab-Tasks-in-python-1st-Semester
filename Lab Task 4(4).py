name = input("Enter your name : ")
fname = input("Enter your Father's name : ")
rno = input("Enter your roll number : ")
subjects = ["maths", "physics", "chemistry", "computer", "Bio"]
tmarks = 0
for i in subjects:
    marks = int(input("Enter marks : "))
    tmarks = tmarks + marks
if tmarks <= 100 or tmarks >= 90:
        grade = "A+"
elif tmarks < 90  or tmarks >= 80:
        grade = "A"
elif tmarks < 80 or tmarks >= 70:
        grade = "B"
elif tmarks < 70 or tmarks >= 60:
        grade = "C"
else:
    grade = "D"
per = (tmarks/500)*100
print("", name,"\n",fname,"\n",subjects,"\n",grade,"\n",per)