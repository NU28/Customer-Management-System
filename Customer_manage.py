# This is Customer Management System Program
# Note: this program is based on list that if you can add details so that details is exist if program is in execution


listid=[]
listname=[]
listmob=[]
listage=[]
listprint=[]

# Add new customer
def add(ai,an,aa,am):
    listid.append(ai)
    listname.append(an)
    listage.append(aa)
    listmob.append(am)
    return (id,name,age,mob)
# Modify existing customer
def mod(mi,mn,ma,mm):
    listname[mi]=mn
    listage[mi]=ma
    listmob[mi]=mm
    return (ind,name,age,mob)
# Remove existing customer
def dele(i):
    listid.pop(i)
    listname.pop(i)
    listage.pop(i)
    listmob.pop(i)
    return (ind)
while(1):
    # Operations print that User can perform
    print("\n-*-*-*-*-*-*-*-CMS Program by Nitin Upadhyay-*-*-*-*-*-*-*-\n\n 1) Add a new Customer Information.\n2) Show all customer details.\n3) Edit an existing customer.\n4) Remove an existing customer.\n5) Search an existing customer.\n6) Exit!")
    c=(input())
    if len(c)<=0 or c.isalpha():
        print("Please enter Numeric Choice.","Please enter choice from above.")
    elif(c<='0' or c>='7'):
        print("Please enter valid choice.")

    # Exit from program
    elif(c=='6'):
        print("Good Bye!")
        break

    # Further Operations
    else:
        # Add New Customer Info
        if(c=='1'):
            while(1):
                # For ID checker.
                while(1):
                    while(1):
                        id = input("\nEnter Customer ID (Numeric value only): ")
                        if id not in listid:
                            break
                        else:
                            print("The Id you are entered is exist. Please try again.")
                    if len(id) <= 0:
                        print("Null value is not allowed. ",end='')
                    if id.isnumeric() :
                        if len(id)==5:
                            break
                        else:
                            print("Please enter valid customer id (Only 5 Digit).")
                    else:
                        print("Please enter numeric value.")

                # For name checker
                while(1):
                    name = input("Enter Customer's Name: ")
                    if len(name) == 0:
                        print("Null value is not allowed. ",end='')
                    if name.isalpha():
                        if len(name) < 4 or len(name) > 20:
                            print("Please enter valid customer name.")
                        else:
                            break
                    else:
                        print("Please enter alphabetic value.")
                # For age checker
                while(1):
                    age = input("Enter Customer's Age: ")
                    if age.isnumeric():
                        if len(age)==2 or len(age)==3:
                            break
                        else:
                            print("Entered Customer age is invalid. Please enter again.")
                    else:
                        print("Please enter numeric value.")
                # For mobile no. checker
                while(1):
                    while(1):
                        mob = input("Enter Customer's Mobile no.: ")
                        if mob not in listmob:
                            break
                        else:
                            print("The Mobile no. you are entered is exist. Please give me different mobile no.")
                    if mob.isnumeric():
                        if len(mob)==10:
                            break
                        else:
                            print("Entered Customer mobile no. is invalid. Please enter again.")
                    else:
                        print("Please enter numeric value.")
                add(id,name,age,mob)
                print("\nCustomer Added Successfully.")
                c=input("Do u want to add more customer (Y/N): ")
                if c=='n' or c=='N':
                    break
                elif c == 'y' or c == 'Y':
                    pass
                else:
                    print("You entered other than (Y/N) input. Good Bye!")
                    break
        # Show all Customer info
        elif(c=='2'):
            print("\nCustomer ",len(listid), "Details :-\n")
            print("Customer ID \t Customer Name \t Customer Age \t Customer mobile no.")
            for i in range(len(listid)):
                print(listid[i],"\t".expandtabs(10),listname[i],"\t".expandtabs(9),listage[i],"\t".expandtabs(12),listmob[i])
        # Edit existing customer
        elif(c=='3'):
            while(1):
                id=input("Enter customer ID: ")
                if id in listid and id.isnumeric():
                    ind=listid.index(id)
                    while (1):
                        name = input("Enter New Customer's Name: ")
                        if len(name) == 0:
                            print("Null value is not allowed. ", end='')
                        if name.isalpha():
                            if len(name) < 5 or len(name) > 9:
                                print("Please enter valid customer name in range(5-20).")
                            else:
                                break
                        else:
                            print("Please enter alphabetic value.")
                    while (1):
                        age = input("Enter New Customer's Age: ")
                        if len(age) <= 0:
                            print("Null value is not allowed. ", end='')
                        if age.isnumeric():
                            if len(age) == 3 or len(age)==2:
                                break
                            else:
                                print("Entered Customer age is invalid. Please enter again.")
                        else:
                            print("Please enter numeric value.")
                    while (1):
                        while (1):
                            mob = input("Enter Customer's Mobile no.: ")
                            if mob not in listmob:
                                break
                            else:
                                print("The Mobile no. you are entered is exist. Please give me different mobile no.")
                        if mob.isnumeric():
                            if len(mob) == 10:
                                break
                            else:
                                print("Entered Customer mobile no. is invalid. Please enter again.")
                        else:
                            print("Please enter numeric value.")
                    mod(ind, name, age, mob)
                    print("\nModification of customer info is done Successfully.")
                    c = input("Do u want to modify more customer (Y/N): ")
                    if c == 'n' or c == 'N':
                        break
                    elif c=='y' or c=='Y':
                        pass
                    else:
                        print("You entered other than (Y/N) input. Good Bye!")
                        break
                else:
                    print("Enter customer id is either not valid or doesn't exist. Please try again.")
        # Remove existing customer
        elif(c=='4'):
            while (1):
                id = input("Enter customer ID: ")
                if id in listid and id.isnumeric():
                    ind = listid.index(id)
                    dele(ind)
                    print("Customer is deleted successfully.")
                    c = input("Do u want to modify more customer (Y/N): ")
                    if c == 'n' or c == 'N':
                        break
                    elif c=='y' or c=='Y':
                        pass
                    else:
                        print("You entered other than (Y/N) input. Good Bye!")
                        break
                else:
                    print("Enter customer id is either not valid or doesn't exist. Please try again.")
        # Search Existing customer
        elif(c=='5'):
            while(1):
                id=input("Enter Customer ID: ")
                if id in listid:
                    ind=listid.index(id)
                    print("Customer ID: ",listid[ind])
                    print("Customer Name: ",listname[ind])
                    print("Customer age: ",listage[ind])
                    print("Customer Mobile no.: ",listmob[ind])
                    c = input("Do u want to search more customer (Y/N): ")
                    if c == 'n' or c == 'N':
                        break
                    elif c=='y' or c=='Y':
                        pass
                    else:
                        print("You entered other than (Y/N) input. Good Bye!")
                        break
                else:
                    print("Enter customer id is either not valid or doesn't exist. Please try again.")