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
        
        def init(self, fun):
            self._init = fun
    
        def destroy(self):
            pass

        def start(self, trigger = lambda: True):
            self._trigger = trigger
            if hasattr(self, '_init'):
                self._init()
            super().start()

        def run(self):
            while not self.stopped():
                self._trigger()
                func()

        def suspend(self):
            print("Suspend")

        def terminate(self):
            print("Terminate")

    return WorkerThread()
