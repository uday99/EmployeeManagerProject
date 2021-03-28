# EmployeeManagerProject
EmployeeManagerProject


welcome to project Description 
==============================
Requirements

Python 3.9.2

Package             Version
------------------- -------
asgiref             3.3.1
Django              3.1.7
django-filter       2.4.0
djangorestframework 3.12.4
Markdown            3.3.4
mysqlclient         2.0.3
pip                 21.0.1
pytz                2021.1
setuptools          54.2.0
sqlparse            0.4.1

Pycharm IDE for project development
=====================================
-->created new project using pycharm 
   1)project and app--MydjangoProj
   2) Set the python interpreter path in your pycharm
   3) download all the given above packages in your pycharm
   4) Start django project
   5) In setting.py file modifiy databse setting  to default mySql 
   4) In setting.py  take rest_framework app in Installed apps
   5) create database with mycompany name



Databases
==========
Install mysql in your system
use mysqlcommand client 

------->create database  mycompany;
------->use mycompany database;

check any tables are created in your database using command---->show tables;
 


In your pycharm Terminal 
=======================
    1) After modifiying all settings in settings.py and creation of database in mysqlclient-IN terminal---->python manage.py makemigrations(create tables)
                                                                                                       ---->python manage.py migrate(migrated to specific database)
     

    2) Compile the code using server ----python manage.py runserver 


project description:
====================
  This is purely build using python and Django restFramework (DRF)

 This is Manager employee project  where manager signIN using a url and creates a profile using url and manager login into using the 
  credential username and password 
 

  if the manager logged in successfully it show -->successfully logged in
  els it gives a message as incorrect user name and password





     urls:
============
  server takes you to browser to execute the projects use all the following urls for different operations

  1)  MangerSignIN -use-->http://127.0.0.1:8000/manager-signIn/



  2)  Manger login -use -->http://127.0.0.1:8000/manager_login/

       if the manager logged in successfully it show -->successfully logged in
  els it gives a message as incorrect user name and password

  3) After manager login successfully a session is created for manager so that he can use to add employees
     
    if manager is not logged /session is not created su it doesnt allow anyone to perform operations on employee.
   
     if manager logged in successfully he can perform all below operations
 
     
     1>Create EMPloyee
          To create employee--->http://127.0.0.1:8000/create_employee/




     2>view all employees in sorted order using first and lastname--->http://127.0.0.1:8000/view_allemployees/





      3) perform update,delete operations use--->http://127.0.0.1:8000/employee_opers/<pk>(idno)

      4)mangaer logoout use-->

     




 


     
