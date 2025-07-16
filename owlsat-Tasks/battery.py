'''

Checks battery life

Take code from Power in the old github? https://github.com/OWLSAT/Power

'''

from Tasks.template_task import Task

class task(Task):
    priority = 1
    frequency = 1 # once every second
    name = 'battery'
    color = 'yellow'

    async def main_task(self):
        print('battery start')