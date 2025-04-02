'''

This is the watchdog reset program.
It sends a pulse to the hardware so it doesn't manually reset the satellite thinking it crashed.

test
'''

from Tasks.template_task import Task

class task(Task):
    priority = 1
    frequency = 1/4 # once every 4s
    name = 'watchdog'
    color = 'red'

    async def main_task(self):
        print('watchdog start')