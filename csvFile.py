import csv

NewFile = open("test.csv", 'w+', newline='')
NewFileWriter = csv.writer(NewFile)
NewFileWriter.writerow(['Roll Number', 'Name', 'Class'])

while True:
    ch = input("Do you want to insert new record? (y/n): ")
    if ch.lower() == 'y':
        rn = int(input("Enter the Roll No.: "))
        nm = input("Enter the name: ")
        cl = int(input("Enter the class: "))
        write_list = [rn, nm, cl]
        NewFileWriter.writerow(write_list)
    else:
        break


NewFile.close()
NewFile = open('test.csv', 'r')


creader = csv.reader(NewFile)
for rec in creader:
    print(rec)
