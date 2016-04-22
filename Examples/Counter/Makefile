all: clean gen_hwd_code simulate

gen_hwd_code: counter32.py
	python counter32.py

simulate: counter32.py counter32_tb.py
	python counter32_tb.py
	gtkwave test_Counter32.vcd


clean:
	rm -rf *.v *.vhd *.pyc *.vcd*

PHONY: all clean
