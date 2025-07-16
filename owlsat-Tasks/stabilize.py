'''

Use the gyroscope to keep the satellite stable in orbit.

Take code from ADCS Sim in the old github?: https://github.com/OWLSAT/ADCS-Sim

'''

from Tasks.template_task import Task

class task(Task):
    priority = 2
    frequency = 1/5 # once every 5s
    name = 'stabilize'
    color = 'green'

    async def main_task(self):
        print('stabilize start')