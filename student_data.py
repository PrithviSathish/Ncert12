import pickle

file = open("student.dat", "ab+")

def add_record(rn, nm):
    new_rec = {"Roll No": rn, "Name": nm}
    pickle.dump(new_rec, file)

def display_record():
    print("----- STUDENT INFO -----")
    print("Roll Number\tName")
    file.seek(0)
    while True:
        try:
            read_rec = pickle.load(file)
            print(f"{read_rec['Roll No']}\t\t{read_rec['Name']}\n")
        except EOFError:
            print("Error")
            break

def search_record(search):
    file.seek(0)
    while True:
        try:
            read_rec = pickle.load(file)
            if read_rec["Roll No"] == search:
                print(f"Roll No: {search}\t\tName: {read_rec['Name']}")

        except EOFError:
            break

def update_record(rn, new_name):
    file = open('Student.dat','rb+')
    file.seek(0)
    while True:
        try:
            pos = file.tell()
            s = pickle.load(file)
            if s[0] == rn:
                print('The searched Roll no. is found and details:',s)
                s[1] = new_name
                file.seek(pos)
                pickle.dump(s,file)
                print('Updated successfully')
                print(s)
                break 
        except EOFError:
            print('Roll no. not found')


update_record(2, "new bye")
display_record()
file.close()
