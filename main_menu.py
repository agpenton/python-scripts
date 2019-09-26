#Netflix type system demo - FakeFlix
import csv
import sys
import string #for use in the secure password and other parts of the program

def main():
    menu()

def menu():
    print("************Welcome to FakeFlix Demo**************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        register()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def long_enough(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 6

def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12

def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0

def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0

def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0

def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0

def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True


def register():

    #user is prompted to input all the required fields
    print("Enter first name")
    global firstname
    firstname=input()
    print("Enter surname")
    global surname
    surname=input()
    print("Enter Date of Birth Format: dd/mm/yy")
    global dob
    dob=input()
    print("Enter first line of address")
    global firstlineaddress
    firstlineaddress=input()
    print("Enter Postcode")
    global postcode
    postcode=input()
    print("Enter Gender")
    global gender
    gender=input()
    print("Enter main genre of interest")
    global interest
    interest=input()
    print("Enter email address")
    global email
    email=input()
    substring=dob[-4:] #this sets the date of birth (last four characters that is the year) to substring
    print("Your unique username is", firstname+surname+substring)
    global username
    username=firstname+surname+substring

    #secure password checker
    passwordchecker(username)

def passwordchecker(username):
    password=input("Please enter a password - must be secure and meet our format requirements")
    if test_password(password):
        #open the main registration text file
        with open('fakeflixfile.txt','a') as fakeflixfile:
            fakeflixfileWriter=csv.writer(fakeflixfile)
            #append the registration details to the text file
            fakeflixfileWriter.writerow([username,password,firstname,surname,dob,firstlineaddress,postcode,gender,interest,email])
            print("Record has been written to file")
            #change the username to username.txt - we will use this to create a new unique user text file based on each user's username
        username = (username + ".txt")
        #CREATE a new FILE - it will be called the "username" (with the concatenated .txt at the end)
        file=open(username,'a')
        file.close()
        print("User File has been created")
        fakeflixfile.close()
        menu()
    else:
        passwordchecker(username)


def login():
    #set a variable (boolean type) to true if the user is NOT logged on
    notloggedin="true"
    #while the user is not logged on (i.e. while the login credentials provided do not work ...)
    while notloggedin=="true":
        print("***WELCOME - PLEASE LOGIN")

        #open the file we are reading from
        with open("fakeflixfile.txt",'r') as fakeflixfile:
            #prompt the user to enter their login details
            username=input("Enter username:-")
            password=input("Enter password:-")
            #call upon our reader (this allows us to work with our file)
            fakeflixfileReader=csv.reader(fakeflixfile)
            #for each row that is read by the Reader
            for row in fakeflixfileReader:
                for field in row:

                    #search for the required matches in user entry against what is stored in the file
                    if field==username and row[1]==password:
                        print("Granted")
                        displayfilms(username)
                        notloggedin="false"


global username
#at this stage it becomes necessary to pass the username to the various subs, as we will need it to eventually generate and store viewings for each unique user.
def displayfilms(username):
    print("*******************WELCOME to FAKEFLIX**************************")
    print("Welcome", username, ": ~What would you like to do?~")
    choice = input("""
                      W: Watch a film
                      V: View your Recommendations
                      T: Search by Title
                      R: Search by Rating 
                      Q: Quit FakeFlix

                      Please enter your choice: """)

    if choice == "W" or choice =="w":
        watchfilms(username)
    elif choice == "V" or choice =="v":
        viewrecs()
    elif choice=="T" or choice=="t":
        searchbytitle(username)
    elif choice=="R" or choice=="r":
        searchbyrating(username)
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select from the given options")
        print("Please try again")
        displayfilms(username)

def searchbytitle(username):
    #open the file
    with open("films.txt","r") as f:
        #prompt the user to enter the desired title that they are searching for
        title=input("Enter Title of film:")
        #call up on the csv reader (this will allow us to work with the file and do clever stuff!)
        fReader=csv.reader(f)
        #for reach row that is read by the reader
        for row in fReader:
            #and for each field in that row (this feature is automated by the reader)
            for field in row:
                #if the field is equal to the title that you are looking for
                if title in field: #this looks for title or any part of title in the field (not necessarily a perfect solution)
                    print("Searching file ....please wait")
                    print("Found:", row)
                    print("This is film no:", row[0])

    choice=input("""Would you like to view this film?
                             Y: Yes
                             N: No, thanks

                             Please enter your choice:""")
    if choice=="Y" or choice=="y":
        viewfilmfunction(row[0],username)
    elif choice=="N" or choice=="n":
        displayfilms(username)


def searchbyrating(username):
    #open the file
    with open("films.txt","r") as f:
        #prompt the user to enter the desired title that they are searching for
        rating=input("Enter the RATING you are after *and we'll show you films that match*:")
        #call up on the csv reader (this will allow us to work with the file and do clever stuff!)
        fReader=csv.reader(f)
        #for reach row that is read by the reader
        for row in fReader:
            #and for each field in that row (this feature is automated by the reader)
            for field in row:
                #if the field is equal to the rating that you are looking for
                if rating in field: #this looks for title or any part of title in the field (not necessarily a perfect solution)
                    print("Searching file ....please wait")
                    print("Found:", row)
                    print("This is film no:", row[0])

    choice=input("""Would you like to view any of these films?
                             Y: Yes
                             N: No, thanks

                             Please enter your choice:""")
    if choice=="Y" or choice=="y":
        print("We are taking you to the WATCH FILMS menu - ratings are displayed next to films")
        watchfilms(username)
    elif choice=="N" or choice=="n":
        displayfilms(username)


def watchfilms(username):
    #Open the file for reading
    filmsfile=open("films.txt","r", encoding="utf8")
    #Create a list called displayfilms into which all the file lines are read into....
    displayfilmslist=filmsfile.read()
    #print the list (that now has the film details in it)
    print(displayfilmslist)
    filmsfile.close()
    print("~What would you like to do?~")
    choice = input("""
                      Select a number to View a Film!
                                         or
                      F: Return to the FakeFlix Menu
                      Q: Quit FakeFlix

                      Please enter your choice: """)

    if choice == "F" or choice =="f":
        displayfilms(username)
    elif choice == "Q" or choice =="q":
        sys.exit
    elif choice=="1":
        viewfilmfunction(1,username)
    elif choice=="2":
        viewfilmfunction(2,username)
    elif choice=="3":
        viewfilmfunction(3,username)
    elif choice=="4":
        viewfilmfunction(4,username)
    elif choice=="5":
        viewfilmfunction(5,username)
    elif choice=="6":
        viewfilmfunction(6,username)
    elif choice=="7":
        viewfilmfunction(7,username)
    else:
        print("You must only select from the given options")
        print("Please try again")
        displayfilms()

def viewfilmfunction(x,username):
    #open the file as student file (variable)
    print(username, ":You are about to view Film:", x, "Enter the selection ID number of the film again to confirm viewing")
    with open("films.txt","r") as filmsfile:
        #prompt the user to enter the ID number they require
        idnumber=input("Enter the ID number you require:")
        #call upon our reader (this allows us to work with our file)
        filmsfileReader=csv.reader(filmsfile)
        #for each row that is read by the Reader
        for row in filmsfileReader:
            #and for each field in that row (this does it automatically for us)
            for field in row:
                #if the field is equal to the id number that is being searched for
                if field ==idnumber:
                    #print the row fields (genre and title) corresponding to that ID number
                    #create a list which contains the relevant fields in the row.
                    viewedlist=[row[1],row[2]]
                    print("You have viewed:", viewedlist)
    with open("fakeflixfile.txt","r")as membersfile:
        #Open Reader
        membersfileReader=csv.reader(membersfile)
        for row in membersfileReader:
            for field in row:
                if field==username:

                    #Open Writer to append to file -this time it looks for the file stored by that username
                    with open("%s.txt" % username,"a") as membersfile:

                        membersfileWriter=csv.writer(membersfile)
                        #Use the writer to append the viewedlist to the appropriate member's user file.
                        membersfileWriter.writerow([viewedlist])


        print("Your Recent viewing has been stored")




    print("~Like this film?~")
    choice = input("""
                      ***PRESS L TO LIKE!***
                                         or
                      V: Watch more Films                  
                      F: Return to the FakeFlix Menu
                      Q: Quit FakeFlix

                      Please enter your choice: """)

    if choice == "F" or choice =="f":
        displayfilms(username)
    if choice == "V" or choice =="v":
        watchfilms(username)
    elif choice == "Q" or choice =="q":
        sys.exit
    elif choice=="L" or choice=="l":
        user_like_film(username)
    else:
        print("You must only select from the given options")
        print("Please try again")


import csv
films_file = "films.txt"

def likeafilm(x):
    #open the films file for reading
    with open(films_file,mode="r") as f:
        reader = csv.reader(f)
        #create a list to read in the file (called records) -read in all the rows in the reader
        records = [row for row in reader]
        #and for every record in the list (we are now working with the list not the file)
    for rec in records:
        #print("print rec:", rec) TEST IF NEEDED: This prints all records
        #print("print rec[0]", rec[0]) TEST: this prints the index number for all records, e.g. 0,1,2,3 etc
        #print("print rec[-1]", rec[-1]) TEST: this prints the content of likes (-1 because it is the last one from the end) so 0,0,0, or 3(if the likes are 3)
        #if the index of any of the records is equal to the index number we are searcin for
        if int(rec[0]) ==x:
            #increment that particular field (in the list by 1)
            rec[-1] = str(int(rec[-1]) + 1)
            #open the file for reading, ensure there is a newline inserted on opening to strip any blank spaces or eliminate them so they are not written to the file
    with open("films.txt","w", newline="") as f:
        #write the file (overwrite)
        writer=csv.writer(f)
        #write the new records to the file
        writer.writerows(records)
        print("Your like for Film no:", x, "has been stored - Thanks!")

def user_like_film(username):
    x = int(input("Enter the ID of the film you wish to like: "))
    likeafilm(x)

    print("WANT TO WATCH ANOTHER FILM?")
    watchfilms(username)

main()