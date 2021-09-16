import csv

NewFile = open("Emp.csv", 'a+', newline='')
NewFileWriter = csv.writer(NewFile)
NewFileWriter.writerow(['EmpNo', 'Name', 'Salary'])

while True:
    ch = input("Do you want to insert new record? (y/n): ")
    if ch.lower() == 'y':
        rn = int(input("Enter the Emp No.: "))
        nm = input("Enter the name: ")
        cl = int(input("Enter the Salary: "))
        write_list = [rn, nm, cl]
        NewFileWriter.writerow(write_list)
    else:
        break

NewFile.close()
NewFile = open('Emp.csv', 'r')
emp_search = input("Enter the Emp No: ")

creader = csv.reader(NewFile)
for rec in creader:
    if rec[0] == emp_search:
        print(f"\nEmployee Number: {rec[0]}\nName: {rec[1]}\nSalary: {rec[2]}")
        break
else:
    print("Record not found")
        
