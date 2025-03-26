'''


This is the radio task

This task does several things in order:
- listens for a radio signal
- sends down the sensor and orbit data
- delete all sent data when upload is confirmed

'''

from Tasks.template_task import Task

class task(Task):
    priority = 2
    frequency = 1/10 # once every 10s
    name = 'radio'
    color = 'orange'

    async def main_task(self):
        print('radio start')