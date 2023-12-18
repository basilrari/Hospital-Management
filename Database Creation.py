#Database Creation
import mysql.connector as msq
import tqdm
import time
con=msq.connect(host='localhost',user='root',passwd='student',database='')
cur=con.cursor()
if con.is_connected():
    cur.execute("create database if not exists hospital")
    cur.execute("use hospital")
    cur.execute("create table patients\
                (P_ID varchar(7) primary key not null,\
                    P_Name varchar(25),\
                        P_Age int(3),\
                            P_Gender varchar(10),\
                                P_Address varchar(100),\
                                    P_PhNo varchar(15));")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Patients Successfully Created")
    cur.execute("create table Staff\
                (S_ID varchar(5) primary key not null,\
                    S_Name varchar(25),\
                        S_Desig varchar(15),\
                            S_Age int(3),\
                                S_Gender varchar(15),\
                                    S_PhNo varchar(15),\
                                        S_Address varchar(100),\
                                            S_Dept varchar(25));")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Staff Successfully Created")
    cur.execute("create table Pharmacy\
                (Med_ID varchar(7) primary key not null,\
                    Med_Name varchar(30),\
                                Med_Price int(5));")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Pharmacy Successfully Created")
    cur.execute("create table Services\
                (S_ID varchar(10) primary key not null,\
                    S_Name varchar(25),\
                        S_Price int(5));")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Services Successfully Created")
    cur.execute("create table Appointments\
                (A_ID varchar(10) PRIMARY KEY NOT NULL,\
                    P_ID varchar(7) not null,\
                       S_ID varchar(10),\
                            App_Date date,\
                                App_Time varchar(5),\
                                    P_Name varchar(30),\
                                        P_PhNo varchar(12));")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Appointments Successfully Created")
    cur.execute("Create Table Admission(Ad_ID varchar(7) not null primary key,\
                    P_ID varchar(15),\
                         P_NAME varchar(50),\
                            P_PhNo varchar(15),\
                               S_ID varchar(7),\
                                  S_NAME varchar(50),\
                                      R_ID varchar(7),\
                                         Ad_date DATE,\
                                            Ad_Time TIME,\
                                               Dis_Date DATE,\
                                                   Dis_Time TIME);")
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print("Table Admission Successfully Created")
    cur.execute('create table Billing\
                 (P_ID varchar(7) not null,\
                     M_Price int(8) Default 0 ,\
                         S_Price int(8) default 0,\
                             Ad_Price int(8) default 0,\
                                 T_Price int(10) default 0);')
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print('Table Billing Successfully Created')
    cur.execute('Create Table Accounts(BDate date not null,\
                    P_ID varchar(10) not null,\
                        P_Price int(10) not null default 0,\
                            S_Price int(10) not null default 0,\
                                Ad_Price int(10) not null default 0,\
                                    T_Price int(10) not null default 0);')
    for i in tqdm.tqdm(range(50)):
        time.sleep(0.001)
    print('Table Accounts Successfully Created')
    con.commit()
    con.close()
    print("Connection closed")    
else:
    print("Error in connection")