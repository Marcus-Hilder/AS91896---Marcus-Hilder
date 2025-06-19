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
    "JSM" : {
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
        #"add_task"    : add_task,
        #"remove task" : reomve_task,
        "edit task"   : edit_task,
        #"search_user" : user_search,
        #"print all user's"   : show_all,
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
    Choice_list = []
    for key , task_info in task.items():
        Choice_list.append(task_info["title"])
    choice = easygui.choicebox("pick a task" ,"task picker" , choices=Choice_list)
    for key, task_info in task.items():
        if task_info['title'] == choice:
            return key   
def pick():
    if type == "task":
        Choice_list = []
        for key , task_info in task.items():
            Choice_list.append(task_info["title"])
        choice = easygui.choicebox("pick a task" ,"task picker" , choices=Choice_list)
        for key, task_info in task.items():
            if task_info['title'] == choice:
                return key
    elif type == "lables":
        Choice_list = []
        for key  in task.items():
            Choice_list.append(task_info)
        print(Choice_list)
    elif type == "task_item":
        Choice_list = []
        for key , task_info in task.items():
            for property, property_value in task_info.items():
                Choice_list.append(property)
        print(Choice_list)
    elif type == "user":
        print("how tf did u get here")
    
    else:
        return menu()
def user_pick_task_item(index):
    Choice_list = []
    for key , task_info in task.items():
        if key == index:
            for property, property_value in task_info.items():
                Choice_list.append(property)
    print(Choice_list)

    choice = easygui.choicebox("pick a task" ,"task picker" , choices=Choice_list)
    return choice
def num_edit():
        print()
def text_edit():
    print()

    



def edit_task():
    """
    """
    
    print("susceful entered task edit.")
    user_request_task = user_pick_task()
    user_request_task_item = user_pick_task_item(user_request_task)
    print(user_request_task_item)
    if not user_request_task_item == "Status" or not\
          user_request_task_item == "Priority" :
        value = task[user_request_task][user_request_task_item]
        print(f"entered {user_request_task_item} eddit")
        print(value)
        new_value = easygui.enterbox(f"enter new: {user_request_task_item}", \
                                     "",value,)
        print(new_value)
        task[user_request_task][user_request_task_item] = new_value
        if value == new_value:
            easygui.msgbox("warning nothing changed","Warning!")
            return menu()
        else:
            easygui.msgbox(f"the value was updated from:\n {value}\n \
            to: {new_value} ","warning you eddited task")
            return menu()
    elif user_request_task_item == "Status" or \
          user_request_task_item == "Priority" :
        value = task[user_request_task][user_request_task_item]
        print(f"entered {user_request_task_item} eddit")
        print(value)
        
        new_value = easygui.integerbox(f"enter new: {user_request_task_item}", \
                                     "",value,)

    else:
        return menu()
    

menu()