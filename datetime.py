"""
Write a program to enter the deadline for their project.
"""
import datetime
strDeadline=""
totaldays=0
weeks=0
days=0
currentdate=datetime.date.today()
strDeadline=input("Please enter the deadline date (mm/dd/yyyy): ")
deadline=datetime.datetime.strptime(strDeadline,"%m/%d/%y").date()
totaldays=deadline-currentdate
weeks=totaldays.days/7
days=totaldays.days%7
print("You have %d weeks " %weeks+" and %d days " %days+" until your deadline.")