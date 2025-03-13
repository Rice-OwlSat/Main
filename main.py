'''
This is the main function for our OwlSat project, loosely based on / implementing [????]

tasko: https://github.com/Rice-OwlSat/Flight-Software/blob/master/OwlSat%20-%20Flight%20Software/lib/tasko/
--> loop.py is very helpful. Defines schedule and schedule later functions. It also runs the tasks.

'''

import os, tasko
from pycubed import cubesat
#cubesat is a new instance of the pycubed satellite
#will need to replace this with our own cubesat object at some point


#set everything to the same asyncio obj
cubesat.tasko=tasko

# Dict to store scheduled objects by name (for printing out / debugging, in this file at least)
cubesat.scheduled_tasks={}

for file in os.listdir('Tasks'): #loop through the tasks in the task folder
    # remove the '.py' from file name
    file = file[:-3]
    # ignore these files:
    if file in ("") or file.startswith('._'):
        continue

    # auto-magically import the task file
    # exec is literally running the code: import Tasks.file_name, importing the task file into main.
    # !!! change this if we find a better way of doing it
    exec('import Tasks.{}'.format(file))

    # create a helper object for scheduling the task
    # It is running the code: task_obj = Tasks.file_name.task(cubesat), where cubesat is passed in for "self" in the task's code
    task_obj = eval('Tasks.' + file).task(cubesat)

    # schedule the task now or later based on its attributes
    if hasattr(task_obj, 'schedule_later') and getattr(task_obj, 'schedule_later'):
        schedule = cubesat.tasko.schedule_later
    else:
        schedule = cubesat.tasko.schedule

    # schedule each task object and add it to our dict
    # passed into the tasko loop file as hz, coroutine_function, and priority
    cubesat.scheduled_tasks[task_obj.name] = schedule(task_obj.frequency, task_obj.main_task, task_obj.priority)

#The print statement printing scheduled tasks.
#NOTE --> This is the only use for cubesat.scheduled_tasks={}.
#Prints everything it is going to do before actually running tasko
print(len(cubesat.scheduled_tasks),'total')

#start running the tasko loop
cubesat.tasko.run()
