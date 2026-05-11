import random

'''

-> Declare variables to store student information like:
    Student ID 
    Student Name 
    Student Age 
    Quiz Score
    Assignment Score
    Exam Score
    Student Attendance

-> Calculate

    -> Total score
    -> Average Score 

-> Determine Student Passed Or Not based on Average Score above 75 

-> Update Attendance Value by one using Increment 

-> Determine Award Eligibility i.e To Qualify for Award 

    -> Requires high attendance i.e 90 and above

    -> Student Should be Passed

-> Display 

    Student ID 
    Student Name 
    Quiz Score
    Assignment Score
    Exam Score
    Student Attendance

'''
class Student:
    Student_ID = 9382
    Student_Name = "Prajwal Pawar"
    Student_Age = 24
    Quiz_Score = 87
    Assignment_Score = 78
    Exam_Score = 69
    Student_Attendance = 94


total_score = Student.Quiz_Score + Student.Assignment_Score + Student.Exam_Score
average_score = total_score / 3

print(total_score)

print(average_score)

if average_score > 75:
    status = "Student Passed"
else:    
    status = "Student Failed"

print(status)


if Student.Student_Attendance >= 90 and status == "Student Passed":
    award_status = "Student is Eligible for Award"
else:    
    award_status = "Student is Not Eligible for Award"
print(award_status)
