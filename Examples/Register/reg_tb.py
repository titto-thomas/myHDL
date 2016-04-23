from random import randrange
from myhdl import *
from reg import Register

def test_Register():

	# Component instantiation for testing
	Clock = Signal(bool(0))
	reset = Signal(bool(0))
	data_in = Signal(intbv(0)[32:])
	data_out = Signal(intbv(0)[32:])

	Reg_inst = Register( Clock, reset, data_in, data_out)

	# Clock generation
	@always(delay(1))
	def ClkGen():
		Clock.next = not Clock

	# Main input is applied here
	@instance
    	def MainGen():
		reset.next = 1
		data_in.next = 0
        	yield delay(5)
        	reset.next = 0
        	while True:
            		yield delay(randrange(5,10))
			data_in.next = data_in + 1

	return Reg_inst, ClkGen, MainGen

# Run the simulation
def simulate(timesteps):
	tb = traceSignals(test_Register)
	sim = Simulation(tb)
	sim.run(timesteps)

simulate(20000)
