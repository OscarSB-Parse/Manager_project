# Import datetime module to obtain and manage the date formats and obtain the current date 

from datetime import date

# This function allows to register a new user
# Use an if statement to comprobe the username is equal to admin , if not print an error message 
# If username == admin
# Open the user.txt file in reading mode, use a for loop to iterate through the file to split and strip the lines
# Create 2 variables to request to user a new username and a new password
# Open the user.txt file in appending mode to write the new username and the corresponding password in the file

def reg_user():
    
     if username != "admin":

            print("Only the admin is allowed to register new users")
    
     else:

        new_username = input("Please insert a new username: ")
        
        with open("user.txt" , "r+", encoding="utf-8") as user_file:

            for line in user_file:
                 user,psw = line.strip("\n").split(", ")

                 while new_username ==  user:
                      print(f"the username {new_username} inserted is already taken")
                      new_username = input("Please insert a new username: ")
        
        new_password = input("Please insert your password: ")

        confirmation_password = input("Please insert your password again: ")

        if new_password == confirmation_password:
            
            with open("user.txt" , "a+", encoding = "utf-8") as user_file:

                user_file.write("\n"+new_username+", " +new_password)
                print("New user registered")

        while new_password != confirmation_password:

                print("The passwords inserted do not match")
                new_password = input("Please insert your password: ")
                confirmation_password = input("Please insert your password again: ") 


# This function allows to add new tasks
# Import datetime as this module it will be used to obtain the current date 
# Create 6 variables to store the user inputs 
# Open the tasks.txt file in appending mode append the user inputs in the file at the end of the last line using a new line character

def add_task():
    import datetime
     
    user_task = input ("Please, insert your username: ")

    task_title = input("Please specify the task assigned: ")

    task_description = input("Please insert a description of the task: ")

    current_date = date.today().strftime("%d %m %Y")    

    due_date ="13 Oct 2023"

    task_completed ="No" 
    
    with open("tasks.txt" , "a+", encoding="utf-8") as task_file:
        
        task_file.write("\n"+user_task+", "+task_title+", "+task_description+", "+str(current_date)+", "+due_date+", "+task_completed)

    print("Task successfully created")

# This function allows to view all the tasks inside the tasks.txt file
# Open the tasks.txt file in reading mode, reading every single line in the file
# Split the lines using the split() method to assign a value to every fragment 
# Create a variable called (output) to store the results 
# Use the print funnction to see the results displayed on the console 

def view_all():
     
     print("TASKS\n")

     with open("tasks.txt" , "r+", encoding="utf-8") as task_file:

        task_data = task_file.readlines()

        for position , line in enumerate(task_data , 1):

            split_task = line.split(", ")

            output = f"______________________________[{position}]______________________________\n"
            output+= f"Task assigned to:\t{split_task[0]}\n"
            output+= f"Task:\t\t\t{split_task[1]}\n"
            output+= f"Task description:\t{split_task[2]}\n"
            output+= f"Task assigtation date:\t{split_task[3]}\n"
            output+= f"Task due date:\t\t{split_task[4]}\n"
            output+= f"Is the task completed:\t{split_task[5]}\n"
            output+="\n"
            output+="_______________________________________________________________\n"
            print(output)

# This function allows to view  the tasks assigned to a partricular user (The user who loged in)
# Create 2 empty list t differenciate between the total amount of tasks and the tasks that belong to the user who logged in
# Open the task.txt file in reading mode, use a for loop to iretate through the file
# Create a variable to split the lines and append the lines into the all_task list using the append() method
# Use the index to comprobe if the username who logged in match with the user in the file, if so , add the task in personal_task list
# Use a for loop with the enumerate() function to print every task located in the personal_task list 
# Use If/else statement to do the following checkings
# If user do not have task overdue, print the corresponding message
# Else, Create a variable to store the user input and giving the 2 options (1 - Mark the tasks as complete / 2 - Edit the task)
# For both options, use the index to assosiate which part of the task is needed to change ( is the task completed/ user / due date)
# Open the task.txt file in writing mode, each line in the file is a different task in the all_task list
# Use a for loop to iterate through the list and procede to apply the changes carried out in the previous step using the join method 

def view_mine():
     print("TASKS\n")

     personal_tasks = [] 
     all_tasks = []  

     with open('tasks.txt', 'r', encoding='utf-8') as task_file:
          
          for line in task_file:
               single_task = line.split(",")  

               all_tasks.append(single_task)

               if username == single_task[0]:
                    
                    personal_tasks.append(single_task)

     for position, single_task in enumerate(personal_tasks, 1):

          print(f"______________________________[{position}]______________________________\n"
                f"Task assigned to:\t {single_task[0]}\n"
                f"Task:\t\t\t{single_task[1]}\n"
                f"Task description:\t{single_task[2]}\n"
                f"Task assigtation date:\t{single_task[3]}\n"
                f"Task due date:\t\t{single_task[4]}\n"
                f"Is the task completed:\t{single_task[5]}\n"
                "_______________________________________________________________\n"
                )


    
     if not personal_tasks:
          
          print("You have no task overdue, all up to date")

     task_selec = int(input("Enter 0 to return to main menu\nSelect a task number: ")) 

     if task_selec == 0 : 
          pass
     
     else:
          
          current_task = personal_tasks[task_selec - 1 ]  

          print(f"Assigned to: {current_task[0]}\n"
              f"Title:{current_task[1]}\n"
              f"Description: {current_task[2]}\n"
              f"Assigned: {current_task[3]}\tDue: {current_task[4]}\n"
              f"Completed: {current_task[5]}")
          
          choice = int(input("""Select one of the following options:
          (1) - Mark the task as complete
          (2) - Edit the task
          : """))

          if choice == 1:     

               personal_tasks[task_selec - 1][5] = " Yes\n"

               with open ("tasks.txt" , 'w+', encoding='utf-8') as task_file:

                    for line in all_tasks:
                         task_file.write(",".join(line))

               print ("Task completed")

               

          elif choice ==2:  
               
               if personal_tasks[task_selec - 1][5] != "Yes\n":


                    new_usr_assignation = input(f"Insert the new user assigned to complete the task: ")

                    personal_tasks[task_selec - 1][0] = new_usr_assignation

                    with open ("tasks.txt" , 'w+', encoding='utf-8') as task_file:

                         for line in all_tasks:
                              task_file.write(",".join(line))
                    
                    
                    new_due_date = input(f"Insert the new due date: ")

                    personal_tasks[task_selec - 1][4] = new_due_date

                    with open ("tasks.txt" , 'w+', encoding='utf-8') as task_file:

                         for line in all_tasks:
                              task_file.write(",".join(line))
               
               else:

                    print("The task is completed already\nIt is not possible to edit it")
          
          else:

               pass       

# This function allows to display the tasks stadistics creating a new text file called (task_overview.txt)
# Create 4 variables and assign the value 0 by default as they will be user as counters 
# Open the task.txt file in reading mode and use a for loop to iterate through the tasks using the index to know if the task is or not completed
# Use the counter total_tasks to count the amount of tasks there are in the file
# Use if statements to check the previous condition   
# Use a datetime module to obtain the current date and compare with the due date from the file to know whether the task is or not overdue
# Compare the amount of tasks comleted, not completed and overdue with the total task to obtain the stadistics
# Create a new variable called (task_report) to store the results obtained in the previous iterations
# Open a new txt file called task_overview in writing + mode to create it and write in it the report generated 

def task_statistics():
    import datetime
    total_tasks= 0
    total_tasks_completed = 0
    total_tasks_not_completed = 0
    total_tasks_overdue = 0

    with open ("tasks.txt" , 'r+', encoding='utf-8') as task_file:
         
         for line in task_file:
              
              
              line.strip().split(", ")[5]                
              
              total_tasks+=1
                           
              if line.strip().split(", ")[5] == "Yes":
                   
                   total_tasks_completed += 1
              else:

                   total_tasks_not_completed += 1

              date_from_file =line.strip().split(", ")[4] 
              
              date_to_compare = datetime.datetime.strptime(date_from_file,"%d %b %Y") 


              current_date = datetime.datetime.now()  
              

              if date_to_compare < current_date:

                   if line.strip().split(", ")[5]  != "Yes":
                        total_tasks_overdue +=1


    percent_task_incompleted = (total_tasks_not_completed/total_tasks) * 100
    percent_task_overd = (total_tasks_overdue/total_tasks) * 100
    
    task_report = f"""     __________Task Report__________

     Total tasks:\t\t\t {total_tasks}
     Total tasks completed:\t\t {total_tasks_completed}
     Total tasks not completed:\t {total_tasks_not_completed}
     Total tasks overdue:\t\t {total_tasks_overdue}
     Percent tasks incompleted:\t {percent_task_incompleted}
     Percent tasks overdue:\t{percent_task_overd}

     _______________________________"""
    
    with open ("task_overview.txt", "w+", encoding="utf-8") as task_overview:
         task_overview.write(task_report)
     
    print ("""    ______________________
    TASK REPORT GENERATED
    ______________________""")
    
    
# This function allows to display the user stadistics creating a new text file called (user_overview.txt)
# Create an empty variable that will be used as a counter later on in the function and an empty list 
# Open the user.txt file in reading mode, using a for loop to iterate through the file 
# Count the number of users in the txt file adding +1 to the counter
# Create 4 empty variables related to the tasks and use them as a counters
# Open the task.txt file in reading mode, using a for loop to iterate through the file 
# Count the number of lines in the task.txt file adding +1 to the counter
# Use If/Else statements nested in the for loop and the index to comproe whether the task is completed, not completed 
# or assigned to the user who logged in, comparing the index and the values inside the task.txt file
# Use datetime module to obtain the current date and compare with the deadline date stored in the tasks file to know if the task is or not overdue
# Create a dictionary with 0 values by default and use an if statement to chceck if there is any tasks assigned to the user who logged in
# If so, assign the values obtained in the iterations previously done to the different keys of the dictionary 
# Append the dictionary to the empty list created at the first step in the function
# Use a for loop to iterate through the list linking the users with their personal tasks to calculate the stadistics
# Append this information in a new empty list, using the append method
# Creae a variable called (output_file) to store the information obtained in the previous list 
# Use the join() method to display the information in string format
# Open a new txt file called user_overview in writing + mode to create the txt file and write in it the report generated (output_file)

def user_statistics():
     import datetime

     total_number_users = 0

     statistic_list_users = []

     with open('user.txt', 'r+', encoding='utf-8') as user_file:

          for user in user_file:

               total_number_users += 1

               task_assign_user = 0
               all_tasks = 0
               task_completed= 0
               task_not_completed = 0 
               tasks_overdues = 0

               with open('tasks.txt', 'r+', encoding='utf-8') as task_file:

                    for line in task_file:

                         all_tasks += 1

                         if line.strip().split(', ')[0] == user.split(",")[0]:

                              task_assign_user += 1

                              if line.strip().split(', ')[5] == "Yes":

                                   task_completed += 1
                              
                              else:

                                   task_not_completed +=1



                                   date_from_file =line.strip().split(", ")[4] 
              
                                   date_to_compare = datetime.datetime.strptime(date_from_file,"%d %b %Y") 

                                   current_date = datetime.datetime.now() 

                                   if date_to_compare < current_date:

                                        if line[5] != "Yes":

                                             tasks_overdues +=1

               user_personal_stat = {"User":str(),
                                   "Total_user_task": 0,
                                   "Percent_user_tasks": 0,
                                   "Percent_completed_tasks": 0,
                                   "Percent_not_completed_tasks": 0,
                                   "Percent_overdue_tasks": 0}

               if task_assign_user > 0 :

                    user_personal_stat["User"] = user.split(',')[0]

                    user_personal_stat["Total_user_task"] = task_assign_user

                    user_personal_stat["Percent_user_tasks"] = (task_assign_user / all_tasks) * 100

                    user_personal_stat["Percent_completed_tasks"] = (task_completed / task_assign_user ) * 100

                    user_personal_stat["Percent_not_completed_tasks"] = (task_not_completed / task_assign_user ) * 100

                    user_personal_stat["Percent_overdue_tasks"] = (tasks_overdues / task_assign_user ) * 100

               statistic_list_users.append(user_personal_stat)

          content=[]

          for user in statistic_list_users:

               info = f"""
               __________{user["User"]}__________

               Total Tasks:\t {user['Total_user_task']}
               Percent of all tasks assigned to user:\t {round(user['Percent_user_tasks'], 2)}%
               Percent Completed:\t {round(user['Percent_completed_tasks'], 2)}%
               Percent NOT Completed:\t {round(user['Percent_not_completed_tasks'], 2)}%
               Percent Overdue:\t\ {round(user['Percent_overdue_tasks'], 2)}%
               _________________________ """

               content.append(info)

          output_file = f"""
          __________ USER STATISTICS __________
          {" ".join(content)}
          ________________END________________
          """

          with open ("user_overview.txt" , "w+" , encoding='utf-8' ) as user_overview:

               user_overview.write(output_file)
          
          print ("""    ______________________
    USER REPORT GENERATED
    ______________________""")

# This function allows to display the results obtained in the stadistic, on the screem
# Create a variable to store the user input, use a while loop to obtain a valid answer
# Create an empty list to store the data inside the txt file
# Open  user or tasks overview in reading mode and using a for loop to iterate through the file
# Use the append method to insert each line from the txt file into the empty list 
# Print the results on the console using the join method to view the results in a string format without the new line characters
# Break the loop as soon as the results are displayed 

def generate_reports():

     while True:
          user_selection = input("""Please select one of the following options:
          (1) - Display user stadistics on the screem
          (2) - Display tasks stadistics on the screem
          : """)

          if user_selection == "1":

               user_stat_list = []

               with open ("user_overview.txt" , "r+" , encoding='utf-8' ) as user_overview:

                    for line in user_overview:

                         user_stat_list.append(line)

               print("".join(user_stat_list))
               

               break

          elif user_selection == "2":

               task_stat_list = []

               with open ("task_overview.txt" , "r+" , encoding='utf-8' ) as task_overview:

                    for line in task_overview:

                         task_stat_list.append(line)

               print("".join(task_stat_list))

               break


          else:
               print("You have selected an invalid option")

#====Login Section====
# Open the user.txt file and use a for loop to manage the different lines inside the text file
# Create 2 empty lists to store the users and passwords located en in the user.txt file  
# Divide the line in 2 separate variables using the strip() and split() mothods, user for username and psw for password
# As the line has been split in user and psw, add this variables into the respectives empty lists using the append() method
# Create 2 variables (username / password) to store the user input, 
# Use a while loop to comprobe the username inserted by the user is in the user_list as in this list the users from txt file have been appended
# If so, move forward and ask for the password 
# if not, request the username over and over again 
# Ask for the password and use a while loop to probe if the password inserted match with the user previously inserted  relating them by the index
# If the password match with the username (they must be in the same row into the user.txt file), display a log in message
# If not, request the password until this match with the username

user_file =  open("user.txt" , "r+", encoding="utf-8")

user_list = []
passwords_list = []

for line in user_file:

    user,psw = line.strip("\n").split(", ") 
    user_list.append(user)
    passwords_list.append(psw)

user_file.close()

username = input ("Please enter your username: ")

while not username in user_list:

    print("INVALID USERNAME")
    username = input ("Please enter your username: ")

user_position = user_list.index(username) 

password = input ("Please enter your password: ")

while password != passwords_list[user_position]:

    print("INVALID PASSWORD")
    password = input ("Please enter your password: ")

print(f"Log in successfully\nWelcome {username}")


# Once logged in ,display 2 menues depending of the user inserted, one specific menu for the admin and other menu for the rest of the users
# Use If/Elif/Else statements to move forward through the menu displayed
# Depending on the option selected, call the function linked to that option
# Admin will see displayed a different menu for him with 2 more options (display stadistics and generate reports)
# Use nested if statements to probe the user who logged in is the admin, if not , print the corresponding error message 

while True:

    if username == "admin":

        menu = input('''Select one of the following Options below:
r\t - \tRegistering a user
a\t - \tAdding a task
va\t - \tView all tasks
vm\t - \tView my task
gr\t - \tGenerate Report
s\t - \tDisplay Statistics
e\t - \tExit
: ''').lower()

    else:

        menu = input('''Select one of the following Options below:
r\t - \tRegistering a user
a\t - \tAdding a task
va\t - \tView all tasks
vm\t - \tView my task
e\t - \tExit
: ''').lower()
        
    if menu == "a":

         add_task()

    elif menu == "r":

         reg_user()

    elif menu == "va":

         view_all()

    elif menu == "vm":

         view_mine()

    elif menu == "s":

         if username == "admin":
              select_stadistic = (input("""Please select one of the following options:
              (1) - Tasks stadisticts
              (2) - User stadistics
              : """))

              if select_stadistic == "1":
                   task_statistics()

              elif select_stadistic == "2":
                   user_statistics()
              else:
                   print ("You have inserted an invalid entry")
         else:
              print("Only the admin can display the stadistics")
     
    elif menu == "gr":

          if username == "admin":

               generate_reports()
          else:
              print("Only the admin is allowed to generate the reports")
                    
    elif menu == 'e':

          print('Goodbye!!!')
          exit()
