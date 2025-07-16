'''

This is the GPS task, which collects and stores the GPS data.

'''

from Tasks.template_task import Task

class task(Task):
    priority = 3
    frequency = 1/30 # once every 30s
    name = 'orbit'
    color = 'blue'

    async def main_task(self):
        print('orbit start')