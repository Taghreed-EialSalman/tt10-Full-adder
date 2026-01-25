## How it works
A full adder is a combinational circuit that adds two bits and a carry and outputs a sum bit and a carry bit. When we want to add two binary numbers, each having two or more bits,the LSBs can be added by using a half adder.
## How to test
Test it by running all possible inputs and checking if the outputs match the expected values.check the truth table below.

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0   |
| 0 | 0 |  1  |  1  |  0   |
| 0 | 1 |  0  |  1  |  0   |
| 0 | 1 |  1  |  0  |  1   |
| 1 | 0 |  0  |  1  |  0   |
| 1 | 0 |  1  |  0  |  1   |
| 1 | 1 |  0  |  0  |  1   |
| 1 | 1 |  1  |  1  |  1   |

## External hardware
NONE

## Pinout
### Inputs
| Pin     | Name |
|---------|------|
| ui[0]   | A    |
| ui[1]   | B    |
| ui[2]   | Cin    |
| ui[3]   |      |
| ui[4]   |      |
| ui[5]   |      |
| ui[6]   |      |
| ui[7]   |      |

### Outputs
| Pin     | Name |
|---------|------|
| uo[0]   | Sum    |
| uo[1]   | Cout    |
| uo[2]   |      |
| uo[3]   |      |
| uo[4]   |      |
| uo[5]   |      |
| uo[6]   |      |
| uo[7]   |      |

