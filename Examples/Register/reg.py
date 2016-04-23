from myhdl import *
from dff import DFF

# Register top level definition
def Register(
    clk,
    rst,
    reg_in,
    reg_out
):
	# Signals for storing temporary input and output values
	data_in_list = [Signal(bool(0)) for i in range(len(reg_in))]
	data_out_list = [Signal(bool(0)) for i in range(len(reg_out))]
	
	# Slice the input signal into 'bool' type
	@always_comb
	def input_update():
		for i in range(len(reg_in)):
			data_in_list[i].next = Signal(reg_in[i] == 1)

	# Dynamic component instantiation
	DFF_inst = [None for i in range(len(reg_in))]

    	for i in range(len(reg_in)):
        	DFF_inst[i] = DFF( clk, rst, data_in_list[i], data_out_list[len(reg_in)-1-i] )
	
	# Concatenate output signals and apply		
	reg_out_dummy = ConcatSignal(*data_out_list)
	
	@always_comb
	def update_out():
		reg_out.next = reg_out_dummy
			
	return DFF_inst, input_update, update_out


# For generating the VHDL and Verilog code
Clock = Signal(bool(0))
reset = Signal(bool(0))
data_in = Signal(intbv(0)[32:])
data_out = Signal(intbv(0)[32:])

toVHDL(Register, Clock, reset, data_in, data_out)
toVerilog(Register, Clock, reset, data_in, data_out)
