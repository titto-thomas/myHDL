from myhdl import *

# D Flip Flop definition
def Counter32(
    clk,
    rst,
	max_count,
    count
):
	count_var = Signal(intbv(0)[32:])

	@always(clk.posedge)
	def UpdateCounter():
		if rst == 1:
			count_var.next = 0
		else:
			if count_var >= max_count:
				count_var.next = 0
			else:
				count_var.next = count_var + 1;

	@always_comb
	def UpdateOutput():
		count.next = count_var
			
	return UpdateCounter, UpdateOutput


clock = Signal(bool(0))
reset = Signal(bool(0))
max_count = Signal(intbv(0)[32:])
count = Signal(intbv(0)[32:])

toVHDL(Counter32, clock, reset, max_count, count)
toVerilog(Counter32, clock, reset, max_count, count)
