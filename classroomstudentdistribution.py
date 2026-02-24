#Total students
students = 125
  
#student per class
per_class = 30

#Number of full classes
full_classes = students // per_class

#remaining students
remaining_students = students % per_class

print("Full classes formed:",full_classes)
print("Student without a class:",remaining_students)