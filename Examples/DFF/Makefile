all: clean gen_hwd_code simulate

gen_hwd_code: dff.py
	python dff.py

simulate: dff.py dff_tb.py
	python dff_tb.py
	gtkwave test_DFF.vcd


clean:
	rm -rf *.v *.vhd *.pyc *.vcd*

PHONY: all clean
