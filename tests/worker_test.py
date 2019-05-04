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

from ants import worker

import unittest
import time

#
# These tests are probably not the greatest due to timing usages
#
class TestStringMethods(unittest.TestCase):

	# Should be called atleast onces
	def test_basic_start_stop(self):
	    i  = 0
	    @worker
	    def counter():
	    	nonlocal i
	    	i += 1
	   
	    c = counter.start()
	    time.sleep(0.1) # Sleep a little while
	    c.stop()
	    value = i
	    time.sleep(0.1) # Sleep a little while more to make sure we are stopped

	    self.assertTrue(i - value < 2)   # Might be some diff fue to stopping times
	    
	# Setup a worker triggering every second
	def test_start_with_a_trigger(self):
		i = 0
		@worker
		def counter():
			nonlocal i
			i += 1
		c = counter.start(lambda : time.sleep(0.4))
		time.sleep(0.3)
		c.stop()
		self.assertEqual(1, i)

	# Setup a worker with an starting function
	def test_worker_with_starting(self):
		i = 0
		@worker
		def counter():
			nonlocal i
			i += 1

		@counter.starting
		def counter_starting():
			nonlocal i
			i = 5

		counter.start(lambda : time.sleep(0.4))
		time.sleep(0.3)
		counter.stop()
		self.assertEqual(6, i)

	# Setup a worker with an stopping function
	def test_worker_with_stopping(self):
		i = 0
		@worker
		def counter():
			nonlocal i
			i += 1

		@counter.stopping
		def counter_stopping():
			nonlocal i
			i = 0

		c = counter.start()
		time.sleep(0.1)
		val = i
		c.stop()
		time.sleep(0.1).  # Wait a while for the worker to stop
		self.assertTrue(val > 0)
		self.assertEqual(i, 0)



if __name__ == '__main__':
    unittest.main()