import sys
sys.argv


print("Command Line Todo application \n=============================\n \n"

        "Command line arguments: \n -l   Lists all the tasks \n" ,
        "-a   Adds a new task \n -r   Removes an task \n -c   Completes an task")

argument = input()


def argument_reader(arg):
    if arg == "l":
        return list_of_tasks()
    else:
        print("Hey, use the given arguments")

def list_of_tasks():
    tasks = [{'checked',"learn to code"}, {'unchecked',"read the styleguide"}, {'unchecked',"watch the news"}]
    print(tasks) 

argument_reader(argument)