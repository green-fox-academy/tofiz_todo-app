import sys
argument = sys.argv


print("Command Line Todo application \n=============================\n \n"

        "Command line arguments: \n -l   Lists all the tasks \n" ,
        "-a   Adds a new task \n -r   Removes an task \n -c   Completes an task")

def argument_reader(arg):
    if arg == "l":
        return convert_txt_to_data()
    else:
        print("Hey, use the given arguments")

def convert_txt_to_data():
    f = open("tasks.txt", "r")
    full_text = f.readlines()
    task = []
    for line in full_text:
        task.append(line)
    return task

def done_or_upcoming_selector(task):
    dones = ""
    upcomings = ""
    for element in task:
        if element[:1] == "1":
            dones += element[2:]
            
        elif element[:1] == "0":
            upcomings += element[2:]
            
    return dones, upcomings

   
def list_tasks(d, u):
    print(u)

dones, upcomings = done_or_upcoming_selector(argument_reader(argument[1]))
task = convert_txt_to_data()
list_tasks(dones, upcomings)