from random import randrange
from myhdl import *
from counter32 import Counter32

def test_Counter32():
	clock = Signal(bool(0))
	reset = Signal(bool(0))
	max_count = Signal(intbv(0)[32:])
	count = Signal(intbv(0)[32:])

	Counter32_inst = Counter32 (clock, reset, max_count, count)

	@always(delay(1))
	def ClkGen():
		clock.next = not clock

	@instance
	def MainGen():
		reset.next = 1
		yield delay(25)
		reset.next = 0
		while True:
		    yield delay(randrange(1000, 1500))
		    max_count.next = 40
		    yield delay(randrange(200, 600))
		    max_count.next = 200

	return Counter32_inst, ClkGen, MainGen

def simulate(timesteps):
	tb = traceSignals(test_Counter32)
	sim = Simulation(tb)
	sim.run(timesteps)

simulate(20000)
