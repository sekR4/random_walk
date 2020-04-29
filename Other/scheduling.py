# This script should run similiar like cron job but from my windows laptop.
# The goal is it to automate some of my processes locally without the windows
# task manager what i can't use appropriately due to the lack of admin rights.

import schedule
import time
import os

# inspired by
# https://schedule.readthedocs.io/en/stable/
# https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/deluge_preventsuspendplus/core.py
# https://stackoverflow.com/questions/57647034/prevent-sleep-mode-python-wakelock-on-python


class WindowsInhibitor:
    """https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx"""
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001

    def __init__(self):
        pass

    def inhibit(self):
        import ctypes
        print('Inhibit (prevent) suspend mode')
        ctypes.windll.kernel32.SetThreadExecutionState(
            WindowsInhibitor.ES_CONTINUOUS | WindowsInhibitor.ES_SYSTEM_REQUIRED)


# does this prevent windows from sleeping?
if os.name == 'nt':
    osSleep = WindowsInhibitor()
    osSleep.inhibit()


def test_job():
    print("I'm working...")


schedule.every(1).minutes.do(test_job).tag('test')
# schedule.every(10).seconds.do(test_job).tag('test')

while True:
    schedule.run_pending()
    time.sleep(1)

# schedule.clear('test')
