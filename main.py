import easygui

task = {
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
        "Assignee" : "JLO",
        "Priority" : 1,
        "Status"   : "Blocked"
    }
}

team = {
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
        #"remove task" : reomve_task,
        "edit task"   : edit_task,
        #"search_user" : user_search,
        #"print all user's"   : show_all,
        "view induvigal task" : pick_and_view,
        "view all task"       : view_all,
        "view user task"      : view_user_tasks,
        "exit"        : exit
    }
    get_input = "Y"

    while get_input == "Y":
        msg = "what would you like to do"
        title = "games Database Choices"
        choices = []

        for items in options:
            choices.append(items)
        
        selection = easygui.choicebox(msg , title , choices)
    
        get_input = options[selection]()
def user_pick_task():
    """ allows the user to pick a task then it will return the task for
    the prevous function to handel """
    Choice_list = []
    for key , task_info in task.items():
        Choice_list.append(task_info["title"])
    choice = easygui.choicebox("pick a task" ,"task picker" , choices=Choice_list)
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
    print(Choice_list)
    #present all aviable optins to user then return their choice
    choice = easygui.choicebox("pick a task" ,"task picker" , choices=Choice_list)
    return choice
def user_pick_user():
    """ allows the user to pick a task then it will return the task for
    the prevous function to handel """
    Choice_list = []
    for key , user in team.items():
        Choice_list.append(user["name"])
    choice = easygui.choicebox("pick user" ,"user selsction" , choices=Choice_list)
    for key, user in team.items():
        if user['name'] == choice:
            return key
def edit_task():
    """
    allows user to edit task"""
    user_request_task = user_pick_task()
    user_request_task_item = user_pick_task_item(user_request_task)
    print(user_request_task_item)

    print("susceful entered task edit.")
    user_request_task = user_pick_task()
    user_request_task_item = user_pick_task_item(user_request_task)
    print(user_request_task_item)
    if not user_request_task_item == "Priority" :
        value = task[user_request_task][user_request_task_item]
        print(f"entered {user_request_task_item} eddit")
        print(value)
        new_value = easygui.enterbox(f"enter new: {user_request_task_item}", \
                                     "",value,)
        print(new_value)
        if new_value == None:
            easygui.msgbox("warning nothing changed","Warning!")
            return menu()
        else:
            task[user_request_task][user_request_task_item] = new_value
        if value == new_value:
            easygui.msgbox("warning nothing changed","Warning!")
            return menu()
        else:
            easygui.msgbox(f"the value was updated from:\n {value}\n \
            to: {new_value} ","warning you eddited task")
            return menu()
    #for edditng integers
    elif user_request_task_item == "Status" :
        value = task[user_request_task][user_request_task_item]
        print(f"entered {user_request_task_item} eddit")
        print(value)
        if user_request_task_item == "Status":
            upper = 3
            lower = 1
        else:
            upper = 1
            lower = 5

        new_value = easygui.integerbox(f"enter new: {user_request_task_item}",\
                                     "",value,lower,upper)
        if new_value == None:
            easygui.msgbox("warning nothing changed","Warning!")
            return menu()
        else:
            task[user_request_task][user_request_task_item] = new_value
        if value == new_value:
            easygui.msgbox("warning nothing changed","Warning!")
            return menu()
        else:
            easygui.msgbox(f"the value was updated from:\n {value}\n \
            to: {new_value} ","warning you eddited task")
            return menu()
    else:
        return menu()
def view_user_tasks():
    """ this function allows user to selesct a staff member then view there
     task """
    pretty_format = ""
    user = user_pick_user()
    for key , des in team.items():
        if key == user:
            for k, description in des.items():
                pretty_format += f"{k} : {description}\n"

def new_task():
    print("susceful entered new task.")
    TITLE = "create new task"
    team_names = ['None']
    task_num = 0
    Status = ["Not Started","In Progress","Blocked"]
    
    for key, details in team.items():
        team_names.append(key)
        print(key)
    
    print(team_names)
    task_id = f"T{str(len(task)+1)}"
    n_task_name = easygui.enterbox("enter new task name", TITLE,)
    n_task_description = easygui.enterbox("enter new task description", TITLE,)
    n_task_Assignee = easygui.choicebox("enter new task Assignee", TITLE,\
    team_names)
    n_task_priority = easygui.integerbox("enter task priority",TITLE,2,1,3)
    n_task_status = easygui.choicebox("enter new task status ",TITLE,Status)
    if  n_task_Assignee  != "None" or n_task_status != "completed":
        for key , des in team.items:
            if key == n_task_Assignee:
                team[key]["task"].append(task_id)
    n_task = {
        "title" : n_task_name,
        "description" : n_task_description,
        "Assignee" : n_task_Assignee,
        "Priority" : n_task_priority,
        "Status"   : n_task_status
    }
    task[task_id] = n_task
    view_task(task_id)
    return menu()
def pick_and_view():
    """this function allows the uerser to pick and view a task from
    the task list"""
    pretty_format = ""
    user_request_task = user_pick_task()
    print(user_request_task)
    for key, des in task.items():
        if key == user_request_task:
            for k , info in des.items():
                pretty_format += f"{k} : {info}\n"
    easygui.msgbox(pretty_format)
    return menu()
def view_all():
    pretty_format = ""
    for key, des in task.items():
        for k , info in des.items():
            pretty_format += f"{k} : {info}\n"
    easygui.msgbox(pretty_format)
    return menu()
def view_task(num):
    """this function allows the system to pick and view a task from
    the task list"""
    print("you entred view task")
    print(num)
    gui_output = ""
    for names , data in task[num].items():
        data = f"{names}  :  {data}\n"
        gui_output += data
    easygui.msgbox(gui_output,num)
    return 


menu()
