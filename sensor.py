'''

This is the sensor task, which collects and stores the UV sensor data.

'''

from Tasks.template_task import Task

class task(Task):
    priority = 3
    frequency = 1/30 # once every 30s
    name = 'sensor'
    color = 'magenta'

    async def main_task(self):
        print('sensor start')