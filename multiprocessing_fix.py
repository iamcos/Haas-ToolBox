import multiprocessing.forking
import os
import sys
import queue
import time

class _Popen(multiprocessing.forking.Popen):
    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            # We have to set original _MEIPASS2 value from sys._MEIPASS
            # to get --onefile mode working.
            os.putenv('_MEIPASS2', sys._MEIPASS)
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                # available. In those cases we cannot delete the variable
                # but only set it to the empty string. The bootloader
                # can handle this case.
                if hasattr(os, 'unsetenv'):
                    os.unsetenv('_MEIPASS2')
                else:
                    os.putenv('_MEIPASS2', '')

class Process(multiprocessing.Process):
    _Popen = _Popen

class SendeventProcess(Process):
    def __init__(self, resultQueue):
        self.resultQueue = resultQueue

        multiprocessing.Process.__init__(self)
        self.start()

    def run(self):
       
        self.resultQueue.put((1, 2))
      
	    
def _start():
    while True:
        try:
            command = queue.get_nowait()
        # ... and some more code to actually interpret commands
        except queue.Empty:
            time.sleep(0.015)

def start():
    process = Process(target=_start, args=args)
    process.start()
    return process

if __name__ == '__main__':
    # On Windows calling this function is necessary.
    multiprocessing.freeze_support()

    