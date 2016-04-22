from random import randrange
from myhdl import *
from dff import DFF

def test_DFF():

    Dout, Din, clk, rst = [Signal(bool(0)) for i in range(4)]

    DFF_inst = DFF( clk, rst, Din, Dout )

    @always(delay(10))
    def ClkGen():
        clk.next = not clk

    @always(clk.negedge)
    def ApplyInput():
        Din.next = not Din

    @instance
    def MainGen():
        yield delay(5)
        rst.next = 1
        while True:
            yield delay(randrange(500, 1000))
            rst.next = 0
            yield delay(randrange(80, 140))
            rst.next = 1

    return DFF_inst, ClkGen, ApplyInput, MainGen

def simulate(timesteps):
    tb = traceSignals(test_DFF)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(20000)
