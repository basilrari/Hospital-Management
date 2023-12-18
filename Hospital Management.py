#Hospital Management
print("*****************************************************************")
print("*                                                               *")
print("*                Welcome To Hospital Management                 *")
print("*                                                               *")
print("*****************************************************************")
import mysql.connector as msq
con=msq.connect(host='localhost',user='root',passwd='student',database='hospital')
cur=con.cursor()
cur.execute('set autocommit=1')
x=0
while x==0:
    print("-------------------------------")
    print("|     1:Enter Admin  Mode     |")
    print("|     2:Exit The Software     |")
    print("-------------------------------")
    choice=input("Enter Your Choice : ")
    if choice=='1':
        print("*****************************************")
        print("|         Welcome To Admin Mode         |")
        print("*****************************************")
        x=1
        import stdiomask
        passwd=stdiomask.getpass(prompt="Enter the Password : ",mask="*")
        if passwd=='Admin@1234':
            while x==1:
                print("-------------------------------------")
                print("|         1:Patient Details         |")
                print("|         2:Staff Details           |")
                print("|         3:Pharmacy Details        |")
                print("|         4:Service Details         |")
                print("|         5:Appointment Details     |")
                print("|         6:Admission Details       |")
                print("|         7:Billing / Accounts      |")
                print("|         8:Return To Main Menu     |")
                print("-------------------------------------")
                x=2
                ch=input("Enter your choice : ")
                if ch=='1':
                    while x==2:
                        print("---------------------------------------")
                        print("|        1:Add Patient Details        |")
                        print("|        2:View Patient Details       |")
                        print("|        3:Modify Patient Details     |")
                        print("|        4:Delete Patient Record      |")
                        print("|        5:Back to Previous Menu      |")
                        print("---------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            sql='Select COUNT(P_ID) from Patients;'
                            cur.execute(sql)
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select P_ID from Patients;')
                            rs=cur.fetchall()
                            if n==0:
                                P_ID='P1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[1:])
                                P_ID='P'+str(a+1)
                            P_Name = input("Enter the Patient Name : ")
                            P_Age=int(input("Enter Patient Age : "))
                            P_Gender=input("Enter Patient Gender : ")
                            P_Address=input("Enter Patient Address : ")
                            P_PhNo=input("Enter Patient Phone Number : ")
                            sql="insert into Patients values(%s,%s,%s,%s,%s,%s)"
                            v=(P_ID,P_Name,P_Age,P_Gender,P_Address,P_PhNo)
                            cur.execute(sql,v)
                            print('Record Added Successfully ')
                            print("Your Patient ID is ",P_ID)
                            x=2
                        elif choice=='2':
                            x=4
                            while x==4:
                                print("-----------------------------------------")
                                print("|        1: Use Patient ID as Key       |")      
                                print("|        2: Use Mobile Number as Key    |")
                                print("-----------------------------------------")
                                opt=input("Enter Your Choice : ")
                                if opt=='1':
                                    ids=input("Enter The Patient ID : ")
                                    break
                                elif opt=='2':
                                    ids=input("Enter Mobile Number : ")
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Please Enter Either 1 or 2 ")
                            if choice=='2':
                                if con.is_connected():
                                    cur=con.cursor()
                                    sql="select exists (select * from patients\
                                          where P_ID=%s or P_PhNo=%s)"
                                    idsd=(ids,ids)
                                    cur.execute(sql,(idsd))
                                    rs=cur.fetchall()
                                    if rs[0][0]==0:
                                        print("Patient Record does not exist")
                                        x=2
                                    else:
                                        sql='select * from patients where P_ID=%s or P_PhNo=%s'
                                        idsd=(ids, ids)
                                        cur.execute(sql,idsd)
                                        r=cur.fetchall()
                                        for i in r:
                                            print("Patient ID : ",i[0])
                                            print("Patient Name : ",i[1])
                                            print("Patient Age : ",i[2])
                                            print("Patient Gender : ",i[3])
                                            print("Patient Address : ",i[4])
                                            print("Patient Phone Number : ",i[5])
                                    x=2
                        elif choice=='3':
                            ids = input("Enter the Patient ID : ")
                            if con.is_connected():
                                cur=con.cursor()
                                sql="select exists (select * from patients\
                                      where P_ID=%s or P_PhNo=%s)"
                                idsd=(ids,ids)
                                cur.execute(sql,(idsd))
                                rs=cur.fetchall()
                                if rs[0][0]==0:
                                    print("Patient Record does not exist")
                                    x=2
                                else:
                                    x=3
                                    while x==3:
                                        print("-----------------------------------------")
                                        print("|         1:Edit Patient Name           |")
                                        print("|         2:Edit Patient Age            |")
                                        print("|         3:Edit Patient Gender         |")
                                        print("|         4:Edit Patient Address        |")
                                        print("|         5:Edit Patient Phone No       |")
                                        print("|         6:Go Back                     |")
                                        print("-----------------------------------------")
                                        ch=input("Enter Your Choice : ")
                                        if ch=='1':
                                            nm=input("Enter The Name : ")
                                            sql="update patients\
                                                 set P_Name=%s\
                                                 where P_ID=%s"
                                            v=(nm,ids)
                                            cur.execute(sql,v)
                                            print("Record Updated Successfully")
                                        elif ch=='2':
                                            ag=input("Enter The Age : ")
                                            sql="update patients\
                                                 set P_Age=%s\
                                                 where P_ID=%s"
                                            v=(ag,ids)
                                            cur.execute(sql,v)
                                            print("Record Updated Successfully")
                                        elif ch=='3':
                                            gd=input("Enter The Gender : ")
                                            sql="update patients\
                                                 set P_Gender=%s\
                                                 where P_ID=%s"
                                            v=(gd,ids)
                                            cur.execute(sql,v)
                                            print("Record Updated Successfully")
                                        elif ch=='4':
                                            ad=input("Enter The Address : ")
                                            sql="update patients\
                                                 set P_Address=%s\
                                                 where P_ID=%s"
                                            v=(ad,ids)
                                            cur.execute(sql,v)
                                            print("Record Updated Successfully")
                                        elif ch=='5':                                        
                                            pn=input("Enter The Phone No : ")
                                            sql="update patients\
                                                 set P_PhNo=%s\
                                                 where P_ID=%s"
                                            v=(pn,ids,)
                                            cur.execute(sql,v)
                                            print("Record Updated Successfully")
                                        elif ch=='6': 
                                            x=2
                                            break
                                        else:
                                            print("Invalid choice")
                                            x=3
                        elif choice=='4':
                            ids = input("Enter the Patient ID : ")
                            if con.is_connected():
                                cur=con.cursor()
                                sql="select exists (select * from patients\
                                      where P_ID=%s or P_PhNo=%s)"
                                idsd=(ids,ids)
                                cur.execute(sql,(idsd))
                                rs=cur.fetchall()
                                if rs[0][0]==0:
                                    print("Patient Record does not exist")
                                    x=2
                                else:
                                    sql="Delete from Patients\
                                         where P_ID=%s"
                                    v=(ids,)
                                    cur.execute(sql,v)
                                    print("Record Deleted Successfully")
                                    x=2
                        elif choice=='5':
                            print("Returning To Previous Menu")
                            x=1
                            break
                        else:
                            print("Invalid Choice")
                elif ch=='2':
                    x=2
                    while x==2:
                        print("-----------------------------------------")
                        print("|          1:Add Staff Details          |")
                        print("|          2:View Staff Details         |")
                        print("|          3:Modify Staff Details       |")
                        print("|          4:Delete Staff Details       |")
                        print("|          5:Back to Previous Menu      |")
                        print("-----------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            sql='Select COUNT(S_ID) from Staff;'
                            cur.execute(sql)
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select S_ID from Staff;')
                            rs=cur.fetchall()
                            if n==0:
                                Sid='S1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[1:])
                                Sid='S'+str(a+1)
                            Sname=input("Enter Staff Name : ")
                            Sdesig=input("Enter Staff Designation : ")
                            Sage=int(input("Enter Staff Age : "))
                            Sgender=input("Enter Staff Gender : ")
                            Saddress=input("Enter Staff Address : ")
                            Sphoneno=input("Enter Staff Phone number : ")
                            Sdepartment=input("Enter The Department : ")
                            sql="insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            v=(Sid,Sname,Sdesig,Sage,Sgender,Sphoneno,Saddress,Sdepartment)
                            cur.execute(sql,v)
                            print("Record Added Succesfully")
                            x=2
                        elif choice=='2' or choice=='3' or choice=='4':
                            x=4
                            while x==4:
                                print("-----------------------------------------")
                                print("|       1: Use Staff ID as Key          |")      
                                print("|       2: Use Staff Name as Key        |")
                                print("-----------------------------------------")
                                opt=input("Enter choice : ")
                                if opt=='1':
                                    ids=input("Enter The Staff ID : ")
                                    break
                                elif opt=='2':
                                    ids=input("Enter Staff Name : ")
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Please Enter Either 1 or 2 ")
                            if choice=='2':
                                if con.is_connected():
                                    cur=con.cursor()
                                    sql="select exists (select * from staff\
                                          where S_ID=%s or S_Name=%s)"
                                    idsd=(ids,ids)
                                    cur.execute(sql,(idsd))
                                    rs=cur.fetchall()
                                    if rs[0][0]==0:
                                        print("Invalid Key")
                                    else:
                                        sql='select * from staff where S_ID=%s or S_Name=%s'
                                        idsd=(ids,ids)
                                        cur.execute(sql,idsd)
                                        r=cur.fetchall()
                                        print("Staff ID : ",r[0][0])
                                        print("Staff Name : ",r[0][1])
                                        print("Staff Age : ",r[0][3])
                                        print("Staff Gender : ",r[0][4])
                                        print("Staff Phone Number : ",r[0][5])
                                        print("Staff Address : ",r[0][6])
                                        print("Staff Designation : ",r[0][2])
                                        print("Staff Department : ",r[0][7])
                                    x=2
                            elif choice=='3':
                                x=3
                                while x==3:
                                    print("-----------------------------------------")
                                    print("|         1:Edit Staff Name             |")
                                    print("|         2:Edit Staff Age              |")
                                    print("|         3:Edit Staff Gender           |")
                                    print("|         4:Edit Staff Address          |")
                                    print("|         5:Edit Staff Phone No         |")
                                    print("|         6:Edit Staff Designation      |")
                                    print("|         7:Edit Staff Department       |")
                                    print("|         8:Go Back                     |")
                                    print("-----------------------------------------")
                                    ch=input("Enter Your Choice : ")
                                    if ch=='1':
                                        nm=input("Enter The Name : ")
                                        sql="update staff\
                                             set S_Name=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(nm,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='2':
                                        ag=input("Enter The Age : ")
                                        sql="update staff\
                                             set S_Age=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(ag,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='3':
                                        gd=input("Enter The Gender : ")
                                        sql="update staff\
                                             set S_Gender=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(gd,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='4':
                                        ad=input("Enter The Address : ")
                                        sql="update staff\
                                             set S_Address=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(ad,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='5':                                        
                                        pn=input("Enter The Phone No : ")
                                        sql="update staff\
                                             set S_PhNo=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(pn,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='6':
                                        desig=input("Enter The Designation : ")
                                        sql="update staff\
                                             set S_Desig=%s\
                                             where S_ID=%s or S_Name=%s"
                                        v=(desig,ids,ids)
                                        cur.execute(sql,v)
                                    elif ch=='7':
                                        dept=input("Enter The Department : ")
                                        sql="update staff\
                                             set S_Dept=%s\
                                             where S_ID=%s or S_name=%s"
                                        v=(dept,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='8': 
                                        x=2
                                        print("Returning to Previous Menu")
                                        break
                                    else:
                                        print("Invalid choice")
                                        x=3
                            elif choice=='4':
                                sql="Delete from Staff\
                                     where S_ID=%s or S_Name=%s"
                                v=(ids,ids)
                                cur.execute(sql,v)
                                print("Record Deleted Successfully")
                                x=2
                        elif choice=='5':
                            print("Returning To Previous Menu")
                            x=1
                            break
                        else:
                            print("Invalid Choice")
                                    
                elif ch=='3':
                    x=2
                    while x==2:
                        print("-----------------------------------------")
                        print("|           1:Add Meds Details          |")
                        print("|           2:View Meds Details         |")
                        print("|           3:Modify Meds details       |")
                        print("|           4:Delete Meds Details       |")
                        print("|           5:Back to Previous Menu     |")
                        print("-----------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            sql='Select COUNT(Med_ID) from Pharmacy;'
                            cur.execute(sql)
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select Med_ID from Pharmacy;')
                            rs=cur.fetchall()
                            if n==0:
                                Med_ID='M1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[1:])
                                Med_ID='M'+str(a+1)
                            Med_Name=input("Enter The Med Name : ")
                            Med_Price=int(input("Enter The Price : "))
                            sql="insert into pharmacy values(%s,%s,%s)"
                            v=(Med_ID,Med_Name,Med_Price)
                            cur.execute(sql,v)
                            print("Record Added Succesfully")
                            x=2
                        elif choice=='2' or choice=='3' or choice=='4':
                            x=4
                            while x==4:
                                print("-----------------------------------------")
                                print("|        1: Use Med ID as Key           |")      
                                print("|        2: Use Med Name as Key         |")
                                print("-----------------------------------------")
                                opt=input("Enter choice : ")
                                if opt=='1':
                                    ids=input("Enter The Med ID : ")
                                    break
                                elif opt=='2':
                                    ids=input("Enter Med Name : ")
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Please Enter Either 1 or 2 ")
                            if choice=='2':
                                if con.is_connected():
                                    cur=con.cursor()
                                    sql="select exists (select * from pharmacy\
                                          where Med_Name=%s or Med_Id=%s)"
                                    idsd=(ids,ids)
                                    cur.execute(sql,(idsd))
                                    rs=cur.fetchall()
                                    if rs[0][0]==0:
                                        print("Invalid Key")
                                    else:
                                        sql='select * from pharmacy where Med_Name=%s or Med_ID=%s'
                                        idsd=(ids,ids)
                                        cur.execute(sql,idsd)
                                        r=cur.fetchall()
                                        print("Med ID : ",r[0][0])
                                        print("Med Name : ",r[0][1])
                                        print("Med Price : ",r[0][2])
                                        x=2
                            elif choice=='3':
                                x=3
                                while x==3:
                                    print("-----------------------------------------")
                                    print("|           1:Edit Med Name             |")                                    
                                    print("|           2:Edit Med Price            |")
                                    print("|           3:Go Back                   |")
                                    print("-----------------------------------------")
                                    ch=input("Enter Your Choice : ")
                                    if ch=='1':
                                        nm=input("Enter The Med Name : ")
                                        sql="update pharmacy\
                                             set Med_Name=%s\
                                             where  Med_Name=%s or Med_Id=%s"
                                        v=(nm,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='2':
                                        mp=input("Enter The Price: ")
                                        sql="update  pharmacy\
                                             set Med_Price=%s\
                                             where  Med_Name=%s or Med_Id=%s"
                                        v=(mp,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='3':
                                        print("Returning Back To Previous Menu")
                                        x=2
                                    else:
                                        print("Invalid choice")
                                        x=3
                            elif choice=='4':
                                sql="Delete from pharmacy\
                                    where  Med_Name=%s or Med_Id=%s"
                                v=(ids,ids)
                                cur.execute(sql,v)
                                print("Record Deleted Successfully")
                                x=2
                        elif choice=='5':
                            print("Returning To Main Menu")
                            x=1
                            break
                        else:
                            print("Invalid Choice")
                elif ch=='4':
                    x=2
                    while x==2:
                        print("-----------------------------------------")
                        print("|         1:Add Service Details         |")
                        print("|         2:View Service Details        |")
                        print("|         3:Modify Service Details      |")
                        print("|         4:Delete Service Details      |")
                        print("|         5:Back to Previous Menu       |")
                        print("-----------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            sql='Select COUNT(S_ID) from services;'
                            cur.execute(sql)
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select S_ID from services;')
                            rs=cur.fetchall()
                            if n==0:
                                S_ID='Sv1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[2:])
                                S_ID='Sv'+str(a+1)
                            S_Name=input("Enter The Service Name : ") 
                            S_Price=int(input("Enter The Price : "))
                            sql="insert into services values(%s,%s,%s)"
                            v=(S_ID,S_Name,S_Price)
                            cur.execute(sql,v)
                            print("Record Added Succesfully")
                            x=2
                        elif choice=='2' or choice=='3' or choice=='4':
                            x=4
                            while x==4:
                                print("-----------------------------------------")
                                print("|        1: Use Service ID as Key       |")      
                                print("|        2: Use Service Name as Key     |")
                                print("-----------------------------------------")
                                opt=input("Enter choice : ")
                                if opt=='1':
                                    ids=input("Enter The Service ID : ")
                                    break
                                elif opt=='2':
                                    ids=input("Enter Service Name : ")
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Please Enter Either 1 or 2 ")
                            if choice=='2':
                                if con.is_connected():
                                    cur=con.cursor()
                                    sql="select exists (select * from services\
                                          where S_Name=%s or S_Id=%s)"
                                    idsd=(ids,ids)
                                    cur.execute(sql,(idsd))
                                    rs=cur.fetchall()
                                    if rs[0][0]==0:
                                        print("Invalid Key")
                                    else:
                                        sql='select * from services where S_Name=%s or S_ID=%s'
                                        idsd=(ids,ids)
                                        cur.execute(sql,idsd)
                                        r=cur.fetchall()
                                        print("Service ID : ",r[0][0])
                                        print("Service Name : ",r[0][1])
                                        print("Service Price : ",r[0][2])
                                        x=2
                            elif choice=='3':
                                x=3
                                while x==3:
                                    print("-----------------------------------------")
                                    print("|           1:Edit Service Name          |")
                                    print("|           2:Edit Service Price         |")
                                    print("|           3:Go Back                    |")
                                    print("-----------------------------------------")
                                    ch=input("Enter Your Choice : ")
                                    if ch=='1':
                                        nm=input("Enter The Service Name : ")
                                        sql="update Services\
                                             set S_Name=%s\
                                             where  S_Name=%s or S_ID=%s"
                                        v=(nm,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                    elif ch=='2':
                                        mp=input("Enter The Price: ")
                                        sql="update  services\
                                             set S_Price=%s\
                                             where  S_Name=%s or S_Id=%s"
                                        v=(mp,ids,ids)
                                        cur.execute(sql,v)
                                        print("Record Successfully Updated")    
                                    elif ch=='3':
                                        print("Returning To Previous Menu")
                                        x=2
                                    else:
                                        print("Invalid choice")
                            elif choice=='4':
                                sql="Delete from services\
                                    where  S_Name=%s or S_Id=%s"
                                v=(ids,ids)
                                cur.execute(sql,v)
                                print("Record Successfully Deleted")
                                x=2
                        elif choice=='5':
                            print("Returning To Previous Menu")
                            x=1
                            break
                        else:
                            print("Invalid Choice")         
                elif ch=='5':
                    x=2
                    while x==2:
                        print("------------------------------------------")
                        print("|           1:Book an Appointment        |")
                        print("|           2:View Appointment           |")
                        print("|           3:Modify Appointments        |")
                        print("|           4:Cancel Appintments         |")
                        print("|           5:Back to Previous Menu      |")
                        print("------------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            x=4
                            while x==4:
                                print("------------------------------------------")
                                print("|         1:Existing Patient             |")
                                print("|         2:New Patient                  |")
                                print("------------------------------------------")
                                choice=input("Enter Your Choice : ")
                                if choice=='2':
                                    print("Enter The Patient Details")
                                    sql='Select COUNT(P_ID) from Patients;'
                                    cur.execute(sql)
                                    r=cur.fetchall()
                                    n=r[0][0]
                                    cur.execute('Select P_ID from Patients;')
                                    rs=cur.fetchall()
                                    if n==0:
                                        P_ID='P1000'
                                    else:
                                        x=rs[n-1][0]
                                        a=int(x[1:])
                                        P_ID='P'+str(a+1)
                                    P_Name=input("Enter Patient Name : ")
                                    P_Age=int(input("Enter Patient Age : "))
                                    P_Gender=input("Enter Patient Gender : ")
                                    P_Address=input("Enter Patient Address : ")
                                    P_PhNo=input("Enter Patient Phone Number : ")
                                    sql="insert into Patients values(%s,%s,%s,%s,%s,%s)"
                                    v=(P_ID,P_Name,P_Age,P_Gender,P_Address,P_PhNo)
                                    cur.execute(sql,v)
                                    print('Record Added Successfully')
                                    print("Your Patient ID is ",P_ID)
                                    x=3
                                elif choice=='1':    
                                    P_ID=input("Enter The Patient ID : ")
                                    break
                                
                                else:
                                    print("Invalid Choice")
                            sql='Select COUNT(A_ID) from Appointments;'
                            cur.execute(sql)
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select A_ID from Appointments;')
                            rs=cur.fetchall()
                            if n==0:
                                A_ID='A1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[1:])
                                A_ID='A'+str(a+1)
                            S_ID=input("Enter The Staff ID : ")
                            x=6
                            while x==6:
                                App_Year=input("Enter The Year : ")
                                App_Month=input("Enter The Month : ")
                                App_Day=input("Enter The Day : ")
                                App_Date=App_Year+'-'+App_Month+'-'+App_Day
                                import datetime as dt
                                y=dt.date.today()
                                if str(App_Date) < str(y):
                                    print('Please enter a date in future')
                                    x=6
                                else:
                                    x=3
                            while x==3:
                                App_Time=input("Enter The Time Slot : ")
                                sql='select *  from appointments where app_date=%s and S_ID=%s'
                                ids=(App_Date,S_ID)
                                cur.execute(sql,ids)
                                r=cur.fetchall()
                                if r==[]:
                                    x=5
                                else:
                                    for i in r:
                                        if i[3]==App_Time:
                                            print("------------------------------------------")
                                            print("|          Time Slot Unavailable         |")
                                            print("------------------------------------------")
                                            x=3
                                            break
                                        else:
                                            x=5
                                            continue
                            while x==5:
                                ids=(P_ID,)
                                sql='select * from patients where P_ID=%s'
                                cur.execute(sql,ids)
                                r=cur.fetchall()
                                for i in r:
                                    P_Name=i[1]
                                    P_PhNo=i[5]
                                sql="insert into Appointments values(%s,%s,%s,%s,%s,%s,%s)"
                                v=(A_ID,P_ID,S_ID,App_Date,App_Time,P_Name,P_PhNo)
                                cur.execute(sql,v)
                                print("Record Added Succesfully")
                                print("Your Appintment ID is ",A_ID)
                                x=2
                        elif choice=='2':
                            A_ID=input("Enter The Appointment ID : ")
                            if con.is_connected():
                                cur=con.cursor()
                                sql="select exists (select * from appointments\
                                      where A_Id=%s)"
                                ids=(A_ID,)
                                cur.execute(sql,ids)
                                rs=cur.fetchall()
                                if rs[0][0]==0:
                                    print("Invalid Key")
                                else:
                                    sql='select * from appointments where A_ID=%s'
                                    ids=(A_ID,)
                                    cur.execute(sql,ids)
                                    r=cur.fetchall()
                                    for i in r:
                                        print("Appointment ID : ",i[0])
                                        print("Patient ID : ",i[1])
                                        print("Patient Name : ",i[5])
                                        print("Patient Phone Number : ",i[6])
                                        print("Assigned Doctor ID : ",i[2])
                                        print("Appointment Date : ",i[3])
                                        print("Appoitment Time : ",i[4])
                                    x=2
                        elif choice=='3':
                            A_ID=input("Enter The Appointment ID : ")
                            x=4
                            while x==4:
                                print("-----------------------------------------")
                                print("|        1:Edit Doctor ID               |")
                                print("|        2:Edit Appointment Date        |")
                                print("|        3:Edit Appointment Time        |")
                                print("|        4:Go Back                      |")
                                print("-----------------------------------------")
                                ch=input("Enter Your Choice : ")
                                if ch=='1':
                                    nm=input("Enter The Doctor ID : ")
                                    sql="update Appointments\
                                         set S_ID=%s\
                                         where A_ID=%s"
                                    v=(nm,A_ID)
                                    cur.execute(sql,v)
                                    print("Record Updated Successfully")
                                elif ch=='2':
                                    x=6
                                    while x==6:
                                        App_Year=input("Enter The Year : ")
                                        App_Month=input("Enter The Month : ")
                                        App_Day=input("Enter The Day : ")
                                        App_Date=App_Year+'-'+App_Month+'-'+App_Day
                                        import datetime as dt
                                        Y=dt.date.today()
                                        if str(App_Date) < str(Y):
                                            print('Please enter a date in future')
                                            x=6
                                        else:
                                            x=4
                                    if x==4:
                                        sql="update  Appointments\
                                             set App_Date=%s\
                                             where A_ID=%s"
                                        v=(App_Date,A_ID)
                                        cur.execute(sql,v)
                                        print("Record Updated Successfully")
                                        x=4
                                elif ch=='3':
                                    mp=input("Enter The Appointment Time: ")
                                    sql="update  Appointments\
                                        set App_Time=%s\
                                         where  A_ID=%s"
                                    v=(mp,A_ID)
                                    cur.execute(sql,v)
                                    print("Record Updated Successfully")
                                    x=4
                                elif ch=='4':
                                    x=2
                                else:
                                    print("Invalid choice")
                        elif choice=='4':
                            A_ID=input("Enter The Appointment Id : ")
                            sql="Delete from Appointments\
                                where  A_ID=%s"
                            v=(A_ID,)
                            cur.execute(sql,v)
                            print("Appointment Cancelled Successfully")
                            x=2
                        elif choice=='5':
                            print("Returning To Previous Menu")
                            x=1
                            break
                        else:
                            print("Invalid Choice")
                elif ch=='6':
                    x=2
                    while x==2:
                        print("-----------------------------------------")
                        print("         1:Admission                    |")
                        print("         2:Discharge                    |")
                        print("         3:View Admission Details       |")
                        print("         4:Go Back To Previous Menu     |")
                        print("-----------------------------------------")
                        choice=input("Enter Your Choice : ")
                        if choice=='1':
                            cur.execute('Select COUNT(Ad_ID) from Admission;')
                            r=cur.fetchall()
                            n=r[0][0]
                            cur.execute('Select Ad_ID from Admission;')
                            rs=cur.fetchall()
                            if n==0:
                                AD_ID='Ad1000'
                            else:
                                x=rs[n-1][0]
                                a=int(x[2:])
                                AD_ID='Ad'+str(a+1)
                            P_ID = input("Enter the Patient ID : ")
                            S_ID = input("Enter the Staff ID : ")
                            R_ID = input("Enter The Accomodation ID : ")
                            v=(AD_ID,P_ID,S_ID,R_ID)
                            sql='Insert into Admission(Ad_ID,P_ID,S_ID,R_ID) values(%s,%s,%s,%s);'
                            cur.execute(sql,v)
                            sql='Update admission set P_Name=(select P_Name from Patients where P_ID=%s),\
                                                    P_phno=(select P_Phno from Patients where P_ID=%s)\
                                                        where P_ID=%s;'
                            v=(P_ID,P_ID,P_ID)
                            cur.execute(sql,v)
                            sql='Update admission set S_Name=(select S_Name from Staff where S_ID=%s);'
                            v=(S_ID,)
                            cur.execute(sql,v)
                            import datetime as dt
                            date=dt.date.today()
                            time=dt.datetime.now()
                            sql='Update admission set Ad_Date=%s,Ad_Time=%s where Ad_ID=%s;'
                            v=(date,time,AD_ID)
                            cur.execute(sql,v)
                            print("Patient Admitted Successfully")
                            print("Your Admission ID is ",AD_ID)
                            x=2
                        elif choice=='2':
                            AD_ID =input("Enter the Admission ID : ")
                            import datetime as dt
                            date=dt.date.today()
                            time=dt.datetime.now()
                            sql='Update admission set Dis_Date=%s,Dis_Time=%s where Ad_ID=%s;'
                            v=(date,time,AD_ID)
                            cur.execute(sql,v)
                            print("Patient Discharged Successfully")
                            x=2
                        elif choice=='3':
                            AD_ID=input("Enter The Admission Id : ")
                            cur=con.cursor()
                            sql="select exists (select * from admission\
                                  where AD_Id=%s)"
                            ids=(AD_ID,)
                            cur.execute(sql,ids)
                            rs=cur.fetchall()
                            if rs[0][0]==0:
                                print("Invalid Key")
                            else:
                                sql='select * from admission where AD_ID=%s'
                                ids=(AD_ID,)
                                cur.execute(sql,ids)
                                r=cur.fetchall()
                                for i in r:
                                    print("Admission ID : ",i[0])
                                    print("Patient ID : ",i[1])
                                    print("Patient Name : ",i[2])
                                    print("Patient Phone Number : ",i[3])
                                    print("Staff ID : ",i[4])
                                    print("Staff Name : ",i[5])
                                    print("Accomodation ID : ",i[6])
                                    print("Appointment Date : ",i[7])
                                    print("Appoitment Time : ",i[8])
                                    if i[9]==None:
                                        print("Patient Not Yet Discharged")
                                    else:
                                        print("Discharge Date ; ",i[9])
                                        print("Discharge Time : ",i[10])
                            x=2
                        elif choice=='4':
                            print("Returning To Previous Menu")
                            x=1
                        else:
                            print("Invalid Choice")
                            x=2
                elif ch=='7':
                    x=2
                    while x==2 and con.is_connected():
                        print("-------------------------------------")
                        print("|         1:Pharmacy Billing        |")
                        print("|         2:Service Billing         |")
                        print("|         3:Admission Charges       |")
                        print("|         4:Final Invoice           |")
                        print("|         5:Change Status           |")
                        print("|         6:View Accounts           |")
                        print("|         7:Return To Main Menu     |")
                        print("-------------------------------------")
                        ch=input("Enter Your Choice : ")
                        if ch in ['1','2','3','4']:
                            P_ID=input("Enter The Patient ID : ")
                            sql="select exists (select * from patients\
                                 where P_ID=%s);"
                            cur.execute(sql,(P_ID,))
                            rs=cur.fetchall()
                            if rs[0][0]==0:
                                print("Patient Record Does Not Exist")
                                continue
                            else:
                                sql="select exists (select P_ID from Billing where P_ID=%s);"
                                cur.execute(sql,(P_ID,))
                                r=cur.fetchall()
                                if r[0][0]==0:
                                    sql='insert into Billing(P_ID) values(%s);'
                                    cur.execute(sql,(P_ID,))
                                else:
                                    pass  
                        if ch=='1':
                            s=0
                            x=3
                            while x==3:
                                Med_ID=input("Enter The Medicine ID : ")
                                sql="select exists (select * from pharmacy\
                                    where Med_Id=%s)"
                                cur.execute(sql,(Med_ID,))
                                rs=cur.fetchall()
                                if rs[0][0]==0:
                                    print("Invalid Medicine ID")
                                    x=2
                                else:
                                    Qty=int(input("Enter The Quantity : "))
                                    sql='select Med_Price from Pharmacy where Med_ID=%s;'
                                    v=(Med_ID,)
                                    cur.execute(sql,v)
                                    r=cur.fetchall()
                                    p=r[0][0]
                                    s+=(p*Qty)
                                    sql='update Billing\
                                         Set M_Price=M_Price+%s\
                                             where P_ID=%s;'
                                    cur.execute(sql,(s,P_ID))
                                    ch=input(("Do You Want to Continue? - Y or N-"))
                                    if ch.upper()=='Y':
                                        continue
                                    elif ch.upper()=='N':
                                        x=2
                                    else:
                                        print("Invalid Choice")
                                        print('Returning to Previous Menu')
                                        x=2
                        elif ch=='2':
                            s=0
                            x=3
                            while x==3:
                                S_ID=input("Enter The Service ID : ")
                                sql="select exists (select * from services\
                                     where S_ID=%s)"
                                cur.execute(sql,(S_ID,))
                                rs=cur.fetchall()
                                if rs[0][0]==0:
                                    print("Invalid Service ID")
                                    x=2
                                else:
                                    Qty=int(input("Enter The Quantity : "))
                                    sql='select S_Price from Services where S_ID=%s;'
                                    v=(S_ID,)
                                    cur.execute(sql,v)
                                    r=cur.fetchall()
                                    p=r[0][0]
                                    s+=(p*Qty)
                                    sql='update Billing\
                                         Set S_Price=S_Price+%s\
                                             where P_ID=%s;'
                                    cur.execute(sql,(s,P_ID))
                                    ch=input(("Do You Want to Continue? - Y or N-"))
                                    if ch.upper()=='Y':
                                        continue
                                    elif ch.upper()=='N':
                                        x=2
                                    else:
                                        print("Invalid Choice")
                                        print('Returning to Previous Menu')
                                        x=2
                        elif ch=='3':
                            AD_ID=input("Enter The Admission ID :")
                            sql="select exists (select * from admission\
                                 where AD_Id=%s)"
                            cur.execute(sql,(AD_ID,))
                            rs=cur.fetchall()
                            if rs[0][0]==0:
                                print("Invalid Admission ID")
                                x=2
                            else:
                                Ad_charge=int(input("Enter The Admission Charge : "))
                                R_rent=int(input("Enter The Room Charge : "))
                                sql='select Ad_date,Dis_date from Admission where Ad_ID=%s and Dis_date is NOT NULL;'
                                cur.execute(sql,(AD_ID,))
                                r=cur.fetchall()
                                A_date=r[0][0]
                                D_date=r[0][1]
                                sql='select datediff(%s,%s);'
                                cur.execute(sql,(D_date,A_date))
                                r=cur.fetchall()
                                n=r[0][0]
                                s=Ad_charge+(R_rent*n)
                                sql='update Billing\
                                         Set Ad_Price=Ad_Price+%s\
                                             where P_ID=%s;'
                                cur.execute(sql,(s,P_ID))
                                x=2  
                        elif ch=='4':
                            sql='select * from patients where P_ID=%s'
                            cur.execute(sql,(P_ID,))
                            r=cur.fetchall()
                            for i in r:
                                P_Name=i[1]
                                P_Ads=i[4]
                                P_Phno=i[5]
                            sql='select M_Price,S_Price,Ad_Price from Billing\
                                 where P_ID=%s;'
                            cur.execute(sql,(P_ID,))
                            r=cur.fetchall()
                            Mpr=r[0][0]
                            Spr=r[0][1]
                            Adpr=r[0][2]
                            total=Mpr+Spr+Adpr
                            tax=int(input("Enter The Percentage Tax : "))
                            gtotal=total+(total*tax/100)
                            d = {'|1': ["Pharmacy",Mpr,'|'],
                            '|2': ["Services",Spr,'|'],
                            '|3': ["Admission",Adpr,'|']}
                            import datetime as dt
                            date=dt.date.today()
                            time=dt.datetime.now()
                            ti=time.strftime("%X")
                            l=len(P_Name)
                            m=len(P_Ads)
                            n=len(P_Phno)
                            a=len(str(total))
                            b=len(str(tax))
                            c=len(str(gtotal))
                            print("+----------------------------------------------------------------------------+")
                            print("|                                HOSPITAL                                    |")
                            print("|",date      ,'                                                      ',  ti,'|')
                            print("+----------------------------------------------------------------------------+")
                            print("|Name : ", P_Name,(66-l)*' ','|')
                            print("|Address : ",P_Ads,(63-m)*' ','|')
                            print("|Phone Number : ",P_Phno,(58-n)*' ','|')
                            print("{:<8} {:<15} {:<51} {}".format('|S.No','Department','Total Bill','|'))
                            for k, v in d.items():
                                Dept,Total,x=v
                                print("{:<8} {:<15} {:<51} {}".format(k,Dept,Total,x))
                            print("+----------------------------------------------------------------------------+")
                            print("|Total Amount : ",total,(58-a)*' ','|')
                            print("|Tax : ",tax,'%',(65-b)*' ','|')
                            print("|Amount Payable : ",gtotal,(56-c)*' ','|') 
                            print("+----------------------------------------------------------------------------+")
                            sql='update Billing\
                                 set T_Price=%s\
                                     where p_ID=%s;'
                            cur.execute(sql,(gtotal,P_ID))
                            x=2
                        elif ch=='5':
                            P_ID=input('Enter The Patient ID : ')
                            sql="select exists (select * from patients\
                                 where P_ID=%s);"
                            cur.execute(sql,(P_ID,))
                            rs=cur.fetchall()
                            if rs[0][0]==0:
                                print("Patient Record Does Not Exist")
                            else:
                                sql='Select * from Billing where P_ID =%s;'
                                cur.execute(sql,(P_ID,))
                                r=cur.fetchall()
                                if len(r)!=0:
                                    print('Are You Sure That You Want to Update The Status')
                                    k=input('Input Your choice - Y or N :')
                                    if k.upper()=='Y':
                                        import datetime as dt
                                        date=dt.date.today()
                                        sql='insert into Accounts(BDate,P_ID) values(%s,%s);'
                                        cur.execute(sql,(date,P_ID))
                                        sql='update Accounts A\
                                                Inner Join Billing B ON A.P_ID = B.P_ID\
                                             set A.P_Price=B.M_Price,\
                                                 A.S_Price=B.S_Price,\
                                                     A.Ad_Price=B.Ad_Price,\
                                                         A.T_Price=B.T_Price;'
                                        cur.execute(sql)
                                        sql='Delete from Billing\
                                                 Where P_ID = %s;'
                                        cur.execute(sql,(P_ID,))
                                        print("Status Updated Successfully")
                                    elif k.upper()=='N':
                                        x=2
                                    else:
                                        print('Invalid Choice')
                                        x=2
                                elif len(r)==0:
                                    sql="select exists (select * from ACCOUNTS\
                                              where P_ID=%s);"
                                    cur.execute(sql,(P_ID,))
                                    rs=cur.fetchall()
                                    if rs[0][0]==0:
                                        print('Payment Record Does not exist')
                                    else:
                                        print('Status has Already been Updated')
                        elif ch=='6': 
                            print("-----------------------------------------")
                            print("| View Accounts of                      |")
                            print("|        1: Particular Day              |")      
                            print("|        2: Range of Days               |")
                            print("|        3: Back to Previous Menu       |")
                            print("-----------------------------------------")
                            k=input('Enter Your Choice : ')
                            if k =='1':
                                A_Year=input("Enter The Year : ")
                                A_Month=input("Enter The Month : ")
                                A_Day=input("Enter The Day : ")
                                A_Date=A_Year+'-'+A_Month+'-'+A_Day
                                sql='select * from ACCOUNTS\
                                               where BDate=%s;'
                                cur.execute(sql,(A_Date,))
                                r=cur.fetchall()
                                if len(r)==0:
                                    print('No Payments Accounted on',A_Date)
                                elif len(r)>0:
                                    print('+----------------------------------------------------------------------------------+')
                                    print("{:<8}{:<15}{:<15}{:<15}{:<15}{:<15}{:<19}".format('|','Patient Id','Pharmacy','Service','Admission','Total Bill','|'))
                                    print('+----------------------------------------------------------------------------------+')
                                    for i in r:
                                        d = {'|': [i[1],i[2],i[3],i[4],i[5],'|']} 
                                        for k, v in d.items():
                                            P_id,MP,SP,AP,TP,x=v
                                            print("{:<8}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(k,P_id,MP,SP,AP,TP,x))
                                            x=2
                                        print('+----------------------------------------------------------------------------------+')
                            elif k=='2':
                                A_Year=input("Enter The Year : ")
                                A_Month=input("Enter The Month : ")
                                A_Day=input("Enter The Day : ")
                                Date1=A_Year+'-'+A_Month+'-'+A_Day
                                A_Year=input("Enter The Year : ")
                                A_Month=input("Enter The Month : ")
                                A_Day=input("Enter The Day : ")
                                Date2=A_Year+'-'+A_Month+'-'+A_Day
                                sql='select * from ACCOUNTS\
                                               where BDate between %s and %s;'
                                cur.execute(sql,(Date1,Date2))
                                r=cur.fetchall()
                                if len(r)==0:
                                    print('No Payments Accounted between ',Date1 , 'and', Date2)
                                else:
                                    print('+-------------------------------------------------------------------------------------------------+')
                                    print("{:<8}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format('|','Date','Patient Id','Pharmacy','Service','Admission','Total Bill','|'))
                                    print('+-------------------------------------------------------------------------------------------------+')
                                    for i in r:
                                        d = {'|': [ str(i[0]),i[1],i[2],i[3],i[4],i[5],'|']} 
                                        for k, v in d.items():
                                            da,P_id,MP,SP,AP,TP,x=v
                                            print("{:<8}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(k,da,P_id,MP,SP,AP,TP,x))
                                    print('+-------------------------------------------------------------------------------------------------+')
                                    x=2
                            elif k=='3':
                                x=2
                            else:
                                print('Invalid Choice')
                                print('Returning To Previous Menu')
                                x=2
                        elif ch=='7':
                            print('Returning Previous Menu')
                            x=1
                        else:
                            print('Invaild Choice')
                            print('Returning To Previous Menu')
                            x=1
                elif ch=='8':
                    print("Returning To Main Menu")
                    x=0
                    break
                else:
                    print("Invalid Choice")
                    print("Re-Enter Valid Choice")
                    x=1
        else:
            print("Incorrect Password ")
            print("Please Enter The Correct Password ")
            x=0
    elif choice=='2':
        print("Exitting From Software")
        break
    else:
        print("Invalid Choice")
        print("Enter 1 or 2")