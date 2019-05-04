# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from ants.stoppablethread import StoppableThread
import time

def worker(func):

    class WorkerThread(StoppableThread):
        
        def __init__(self):
            self._starting = lambda: True
            self._stopping = lambda: True
            self._worker = func
            super().__init__()

        def starting(self, fun):
            self._starting = fun
    
        def stopping(self, fun):
            self._stopping = fun

        def destroy(self):
            pass

        def start(self, trigger = lambda: True):
            self._trigger = trigger
            self._starting()
            super().start()
            return self

        def run(self):
            while not self.stopped():
                self._worker()        # Run the worker
                self._trigger()       # Then run the trigger
            self._stopping()         # Finally run stopping function

        def suspend(self):
            print("Suspend")

        def terminate(self):
            print("Terminate")

    return WorkerThread()
