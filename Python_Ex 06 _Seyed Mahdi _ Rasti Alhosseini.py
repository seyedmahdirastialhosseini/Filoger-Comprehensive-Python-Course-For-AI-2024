task_name = []
task_status = []
task_duration = []

def add_task() :
    Name = input(("Say your task name: ")).lower()
    if Name not in task_name :
        task_name.append(Name)
        task_status.append(False)
        task_duration.append(None)
        print("Added!")
    else : print("This task name is repeated!")

def display_all_products() :
    for i , name in enumerate(task_name) :
        print(f"{i+1} , Task Name: {name} , Task Status: {task_status[i]} , Task Duration: {task_duration[i]}")

def remove_task() :
    name_for_remove = input(("Say the task name that you want to remove it: ")).lower()
    if name_for_remove in task_name :
        index = task_name.index(name_for_remove)
        task_name.pop(index)
        task_status.pop(index)
        task_duration.pop(index)
        print("Removed!")
    else : print("Your task name not found!")

def edit_task() :
    name_for_edit = input(("Say the task name that you want to edit it: ")).lower()
    if name_for_edit in task_name :
        new_name = input(("Say the new task name: "))
        if new_name not in task_name : 
            index = task_name.index(name_for_edit)
            task_name[index] = new_name
            print("Edited!")
        else : ("This task name is repeated!")
    else : ("Your task name not found!")

def search_task() :
    name_for_search = input(("Say the task name that you want to search it: ")).lower()
    if name_for_search in task_name :
        index = task_name.index(name_for_search)
        status = task_status[index]
        duration = task_duration[index]
        print(f"Status of you task : {status} , Duration of your task : {duration}.")
    else : ("Your task name not found!")

def mark_task_as_done() :
    name_for_mark = input(("Say the task name that you done it: ")).lower()
    if name_for_mark in task_name :
        index = task_name.index(name_for_mark)
        if task_status[index] == False :
            task_status[index] = True
            duration = float(input("Say the time of you task in hours: "))
            task_duration.insert(index , duration)
        else : print("This task mark done!")
        print("Marked!")
    else : print("Your task name not found!")

def display_details() :
    len_tasks = len(task_name)
    Done = task_status.count(True)
    Undone = task_status.count(False)
    sum_duration = []
    for s in task_duration :
        if s :
            sum_duration.append(s)
    sum_duration1 = sum(sum_duration)
    for i , name in enumerate(task_name) :
        print(f"""Total Tasks: {len_tasks} , Total time of all tasks: {sum_duration1} , Total Done Tasks: {Done} , Total Undone Tasks: {Undone}""")
# Main

for i in range(200) :
    Answer = input(("add task , display all products , remove task , edit task , search task , mark task as done , display details , help , exit ")).lower()

    if Answer == "add task" : 
            add_task()

    elif Answer == "display all products" :
        display_all_products()

    elif Answer == "remove task" :
        remove_task()

    elif Answer == "edit task" :
        edit_task()

    elif Answer == "search task" :
        search_task()


    elif Answer == "mark task as done" :
        mark_task_as_done()

    elif Answer == "display details" :
        display_details()

    elif Answer == "help" :
            print("""
How to use each commend?
                  
add task : you can add your tasks that you want to do them in programme ; you should type the commend and after that , say your task name ; but be careful ; the task name must be unique!
                  
display all products : you can see all tasks in a time ; you can see the number of task , name of task , task status (done or undone) and task duration (in hours)!
                  
remove task : you can remove your task with this commend ,  first you should type the commend and second say you task name that you want to remove it ; but be careful ; your task name you want to remove it must be in task names!
                  
edit task : you can edit a task name with this commend ; for do that , first you should type the commend , second , type the name that you want to edit it , third , type the new task name ; but be careful ; your new name must not be in task names!
                  
search task : you can see the details of a task ; first you should type the commend , second say the task name and after that , you can see the status and duration of your task!
                  
mark task as done : you can mark a task when you done it with this commend ; you should first type the commend , second , type the task that you done it , third , type the time of your task.
                  
display details : you can see all details about your tasks here ; the number of each task and status and the duration of them , in addition to see how tasks took time and which tasks done and which undone ; for use this commend ; you should type the commend first and after that you can see everything!
                  
help : you can see it how to use each commend.""")

    elif Answer == "exit" :
        break
    elif Answer == "" :
        continue
    else : print("Commend not found!") 