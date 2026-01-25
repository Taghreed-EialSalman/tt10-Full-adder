# test/test.py
# Cocotb testbench for Tiny Tapeout project
# Full Adder: inputs A,B,Cin on ui_in[0..2] and outputs Sum,Cout on uo_out[0..1]

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Full Adder verification")

    # Clock: keep Tiny Tapeout template style
    clock = Clock(dut.clk, 10, units="us")  # 100 kHz
    cocotb.start_soon(clock.start())

    # Reset: keep Tiny Tapeout template style (required)
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)

    dut._log.info("Running ALL Full Adder truth-table cases")

    # Full Adder truth table vectors: (A, B, Cin, Sum_expected, Cout_expected)
    test_vectors = [
        # A B Cin | Sum Cout
        (0, 0, 0,   0,  0),  # Case 1
        (0, 0, 1,   1,  0),  # Case 2
        (0, 1, 0,   1,  0),  # Case 3
        (0, 1, 1,   0,  1),  # Case 4
        (1, 0, 0,   1,  0),  # Case 5
        (1, 0, 1,   0,  1),  # Case 6
        (1, 1, 0,   0,  1),  # Case 7
        (1, 1, 1,   1,  1),  # Case 8
    ]

    for idx, (A, B, Cin, Sum_exp, Cout_exp) in enumerate(test_vectors, start=1):
        dut._log.info(
            f"Case {idx}: A={A}, B={B}, Cin={Cin} => expect Sum={Sum_exp}, Cout={Cout_exp}"
        )

        # Apply inputs (per info.yaml pin mapping)
        dut.ui_in[0].value = A
        dut.ui_in[1].value = B
        dut.ui_in[2].value = Cin

        # Wait a few cycles (safe even for combinational; template uses clocked waits)
        await ClockCycles(dut.clk, 10)

        # Check outputs (per info.yaml pin mapping)
        Sum_got = int(dut.uo_out[0].value)
        Cout_got = int(dut.uo_out[1].value)

        assert Sum_got == Sum_exp, (
            f"FAIL Case {idx}: A={A}, B={B}, Cin={Cin} | "
            f"Sum got {Sum_got}, expected {Sum_exp}"
        )
        assert Cout_got == Cout_exp, (
            f"FAIL Case {idx}: A={A}, B={B}, Cin={Cin} | "
            f"Cout got {Cout_got}, expected {Cout_exp}"
        )

    dut._log.info("PASS: All Full Adder test cases passed ✅")
