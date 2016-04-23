all: clean gen_hwd_code simulate

gen_hwd_code: dff.py reg.py
	python reg.py

simulate: dff.py reg.py reg_tb.py
	python reg_tb.py
	gtkwave test_Register.vcd


clean:
	rm -rf *.v *.vhd *.pyc *.vcd* *.*~ *~

PHONY: all clean
