from myhdl import *

# D Flip Flop definition
def DFF(
    clk,
    rst,
    Din,
    Dout
):
	@always(clk.posedge)
	def update():
		if rst == 1:
			Dout.next = 0
		else:
			Dout.next = Din
			
	return update


Clock = Signal(bool(0))
reset = Signal(bool(0))
data_in = Signal(bool(0))
data_out = Signal(bool(0))

toVHDL(DFF, Clock, reset, data_in, data_out)
toVerilog(DFF, Clock, reset, data_in, data_out)
