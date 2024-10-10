# WITI has tasked you to automate a simple grading system
# As  a python student , write a program using to display the grades that
# the students will be recieving based on the mark scored in the subject
# The grades are:
#90%-100%  Grade is A
#80%-89%  Grade is B
#70%-79%  Grade is c
#60%-69% Grade is D
#50%-59% Grade is E
 #<50%fail

if 90<=percent<=100:
   "A"
elif 80<=percent<89:
     "B"
elif 70<=percent<79:
    "C"
elif 60<=percent<69:
    "D"
elif 50<=percent<59:
   "E"
elif 0<=percent<50:
   "F"
else:
  "lnvalid percentage"

name="scovia"
percent=85
grade=percent
print(f"student:{name}")
print(f"percentage:{percent}%")
print(f"grade:{grade}")

