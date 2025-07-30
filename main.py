import easygui

task = {
    #Dict for all tasks
    "T1" : {
        "title" : "Design Homepage",
        "description" : "Create a mockup of the homepage",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status"   : "In Progress"
    },
    "T2" : {
        "title" : "Implement Login page",
        "description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status"   : "Blocked"
    },
    "T3" : {
        "title" : "Fix navigation menu",
        "description" : "Fix the navigation menu to be more user-friendly",
        "Assignee" : "",
        "Priority" : 1,
        "Status"   : "Not Started"
    },
    "T4" : {
        "title" : "Add payment processing",
        "description" : "Implement payment processing for the website",
        "Assignee" : "JLO",
        "Priority" : 2,
        "Status"   : "In Progress"
    },
    "T5" : {
        "title" : "Create an About Us page",
        "description" : "Create a page with information about the company",
        "Assignee" : "BDI",
        "Priority" : 1,
        "Status"   : "Blocked"
    }
}

team = {
    #Dict for all staff members

    "JSM" : {
        "name"  : "john smith",
        "Email" : "John@techvision.com",
        "task"  : ["T1","T2"]
    },
    "JLO" : {
        "name"  : "Jane Love",
        "Email" : "Jane@techvision.com",
        "task"  : ["T4"]
    },
    "BDI" : {
        "name"  : "Bob Dillon",
        "Email" : "Bob@techvision.com",
        "task"  : ["T5"]
    }

}

def menu():
    """
    displays main menu and return user choice
    """
    options = {
        "add_task"    : new_task,
        "edit task"   : edit_task,
        "system search" : system_search,
        "view all task" : view_all,
        "report"        : report,
        "exit"        : exit
    }
    get_input = "Y"

    while get_input == "Y":
        msg = "How can we assist you today"
        title = "Main Menu"
        choices = []

        for items in options:
            choices.append(items)   
        
        selection = easygui.choicebox(msg , title , choices)
        if selection == None:
            exit()
        
        get_input = options[selection]()

def system_search():
    user_request = easygui.buttonbox("search by:", "system search",\
        ("staff member", "task"))
    if user_request == "staff member":
        return view_user_tasks()
    else:
        return pick_and_view()

def user_pick_task():
    """ allows the user to pick a task then it will return the task for
    the prevous function to handel """
    Choice_list = []
    for key , task_info in task.items():
        Choice_list.append(task_info["title"])
    choice = easygui.choicebox("Pick a task" ,f"{len(Choice_list)}\
 tasks to pick from" , Choice_list)
    if choice == None:
        return menu()
    for key, task_info in task.items():
        if task_info['title'] == choice:
            return key   

def user_pick_task_item(index):
    """ allows the user to pick a item in a task then it
    will return the item in the task for the prevous function to handel
    """
    #create a blank list the wright to 
    Choice_list = []
    #scroll throught the list of avible items in the task
    for key , task_info in task.items():
        #check task is = to the task spesified in the prevous function
        if key == index:
            #pull all items from the chosent task and append to list
            for k, des in task_info.items():
                Choice_list.append(k)
    
    #present all aviable optins to user then return their choice
    choice = easygui.choicebox("Pick a task item" ,"Task item picker" ,\
         Choice_list)
    if choice == None:
        return menu()
    else:
        return choice

def user_pick_user():
    """ allows the user to pick a task then it will return the task for
    the prevous function to handel """
    Choice_list = []
    for key , user in team.items():
        Choice_list.append(user["name"])
    choice = easygui.choicebox("Pick user" ,"User selection" , Choice_list)
    if choice == None:
        return menu()
    for key, user in team.items():
        if user['name'] == choice:
            return key
    
def edit_task():
    """
    Allows user to edit a task.
    """
    user = ""  
    # Placeholder to track the user assigned to the task
    selected_task_id = user_pick_task()  
    # User selects which task to edit
    selected_field = user_pick_task_item(selected_task_id)  
    # User selects which attribute to edit

    for name, info in team.items():
        # Identify the user currently assigned to the task
        if selected_task_id in info["task"]:
            user = name

    # Editing title or description
    if selected_field == "title" or\
        selected_field == "description":
        value = task[selected_task_id][selected_field]
        new_value = easygui.enterbox(f"enter new: {selected_field}"\
        , "", value)
        
        # If user dosent change anything edit
        if new_value == None:
            easygui.msgbox("warning nothing changed", "Warning!")
            return menu()
        # If no change was made
        elif value == new_value:
            easygui.msgbox("warning nothing changed", "Warning!")
            return menu()
        else:
            #update the task
            task[selected_task_id][selected_field] = new_value
            #inform the user of what they changed
            easygui.msgbox(f"The value was updated from:\n {value}\n\
to: {new_value} ", "Updating task")
            view_task(selected_task_id)
            return menu()
    
    # Editing status
    elif selected_field == "Status":
        value = task[selected_task_id][selected_field]

        msg = (f"select new status for {selected_task_id}")
        title = (f"update status for {selected_task_id}")
        choices = [f"Completed", "In Progress", "Blocked", "Not Started"]
        new_value = easygui.buttonbox(msg, title, choices)

        task[selected_task_id][selected_field] = new_value
        

        # If task is marked completed, remove it from the team member's
        # task list
        if new_value == "Completed" and user != "":
            assignee = task[selected_task_id]["Assignee"]
            if selected_task_id in team[assignee]["task"]:
                team[assignee]["task"].remove(selected_task_id)
            task[selected_task_id]["Assignee"] = ""

        if value == new_value or value == None:
            easygui.msgbox("warning nothing changed", "Warning!")
            return menu()
        else:
            easygui.msgbox(f"The value was updated from:\n {value}\n \
            to: {new_value} ", "Warning you eddited task")
            view_task(selected_task_id)
            return menu()

    # Editing assignee
    elif selected_field == "Assignee":
        previous_assignee = task[selected_task_id][selected_field]

        staff = [""]
        staff_code = [""]

        # Create name/code mappings for team members
        for key, des in team.items():
            staff.append(des["name"])
            staff_code.append(key)

        # Current assignee position
        pre_set = staff_code.index(previous_assignee) 

        msg = ("Pick New Assignee")
        title = ("New Assignee")
        # Select new assignee
        new_assignee = easygui.choicebox(msg, title, staff, pre_set)  
        index = staff.index(new_assignee)
        # Save new assignee
        
        task[selected_task_id][selected_field] = staff_code[index]  
        
        #up date team dic with user new task and reomove task from 
        #prevous user

        if previous_assignee != new_assignee:
            team[previous_assignee]["task"].remove(selected_task_id)
            team[staff_code[index]]["task"].append(selected_task_id)
        view_task(selected_task_id)
        return menu()

    # Editing priority
    elif selected_field == "Priority":
        value = task[ selected_task_id][selected_field]

        choices = [1, 2, 3]
        pre_set = choices.index(value)
        msg = ("enter new prioity")
        title = ("set new priorty")
        # Select new priority
        new_value = easygui.choicebox(msg, title, choices, pre_set) 
        task[ selected_task_id][selected_field] = new_value
        view_task(selected_task_id)
        return menu()

def view_user_tasks():
    """ 
    This function allows user to select a staff member and view their tasks.
    """
    pretty_format = ""  # String for display
    user = user_pick_user()  # Pick which user to view

    for key, des in team.items():
        if key == user:
            pretty_format += f"{key}\n"
            for title, info in des.items():
                pretty_format += f"{title} : {info}\n"
            
            # Add assigned tasks
            for index, description in task.items():
                if description["Assignee"] == user:
                    pretty_format += f"\n{index}\n"
                    for k, des in description.items():
                        pretty_format += f"{k} : {des}\n"

    easygui.msgbox(pretty_format, f"{user}'s tasks")  # Show message box
    return menu()

def new_task():

    TITLE = "create new task"
    staff_members = ['None']
    Status = ["Not Started", "In Progress", "Blocked"]
    priority = [1, 2, 3]

    # Populate staff choices
    for key, details in team.items():
        staff_members.append(key)

    

    
    task_id = f"T{str(len(task)+1)}"  # Generate new unique incremted task ID

    # Gather task details from user
    while True:
        n_task_name = easygui.enterbox("enter new task name", TITLE)
        if n_task_name == None:
            return menu()
        elif n_task_name != "":
            break
        easygui.msgbox("you cant have a blank title")
    while True:
        n_task_description = easygui.enterbox("enter new task description", TITLE)
        if n_task_description == None:
            return menu()
        elif n_task_description != "":
            break
        easygui.msgbox("you cant have a blank desecrtption")
    n_task_Assignee = easygui.choicebox("enter new task Assignee", TITLE,\
     staff_members)
    if n_task_Assignee == None:
        return menu()
    n_task_priority = easygui.integerbox("enter new task's priority\nBetwen\
         1 and 3", TITLE, None, 1, 3)
    if n_task_priority == None:
        return menu()
    n_task_status = easygui.choicebox("enter new task status ", TITLE, Status)
    if n_task_status == None:
        return menu()

    # If task is assigned and not complete, add to team member's task list
    if n_task_Assignee != "None" or n_task_status != "completed":
        for key, des in team.items():
            if key == n_task_Assignee:
                team[key]["task"].append(task_id)

    # Save task to task dictionary
    n_task = {
        "title": n_task_name,
        "description": n_task_description,
        "Assignee": n_task_Assignee,
        "Priority": n_task_priority,
        "Status": n_task_status
    }
    task[task_id] = n_task
    # Show the newly created task
    view_task(task_id)  
    return menu()

def pick_and_view():
    """this function allows the uerser to pick and view a task from
    the task list"""
    pretty_format = ""
    user_request_task = user_pick_task()

    for key, des in task.items():
        if key == user_request_task:
            for k , info in des.items():
                pretty_format += f"{k} : {info}\n"
    easygui.msgbox(pretty_format)
    return menu()

def view_all():
    """ this function allows the user to see all tasks in system"""
    #int text
    pretty_format = ""
    #run through all task and display in a clear format then prnted by
    #easy gui
    for key, des in task.items():

        pretty_format += f"\n{key}\n"
        for k , info in des.items():
            pretty_format += f" {k} : {info}\n"
    easygui.msgbox(pretty_format,"disply all ")
    
    return menu()

def view_task(num):
    """this function allows the system to pick and view a task from
    the task list"""

    
    gui_output = ""
    for names , data in task[num].items():
        data = f"{names}  :  {data}\n"
        gui_output += data
    easygui.msgbox(gui_output,num)
    return 

def report():
    """ 
    This function allows the user to view all task completion rates.
    It counts the number of tasks in each status category and then 
    displays the results.
    """
    
    # Initialize counters for each task status
    completed = 0
    in_progress = 0
    not_started = 0
    blocked = 0
    
    # Initialize an empty string to build the output message
    pretty_format = ""
   
    # Loop through each task in the 'task' dictionary
    for key, des in task.items():
        
        # Each 'des' is a dictionary of task attributes, loop through 
        # these attributes
        for k, info in des.items():
            
            # Check if the current attribute is the task status
            if k == "Status":
                # Increment the appropriate counter based on the
                # status value
                if info == "Completed":
                    completed += 1
                elif info == "In Progress":
                    in_progress += 1
                elif info == "Blocked":
                    blocked += 1
                elif info == "Not Started":
                    not_started += 1
                else:
                    # If status value is unexpected, print an error 
                    # message
                    print("Unexpected status encountered!")
    
    # Build the summary string to display the counts of each status
    pretty_format += f"Completed : {completed}\n\n"
    pretty_format += f"In Progress : {in_progress}\n\n"
    pretty_format += f"Blocked : {blocked}\n\n"
    pretty_format += f"Not Started : {not_started}"
    task_count = len(task)
    percent_complete = completed / task_count
    blocks_total = 10
    blocks_filled = int(round(percent_complete * blocks_total))

    # Build progress bar string
    progress_bar = "▣" * blocks_filled + "▢" * (blocks_total - blocks_filled)
    # Show the summary to the user using easygui message box
    easygui.msgbox(f"{pretty_format}\n\n {progress_bar} : \
{round(percent_complete*100)}%", "Your current report","KO")
    
    # Return to the menu function after showing the report
    return menu()


menu()
