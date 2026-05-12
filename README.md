# riscv-hanoi-demo


# Tower of Hanoi — RISC-V Code Base Demo

A minimal Python 3 demonstration of recursion using the Tower of Hanoi problem.

## Run
    python3 hanoi.py

## Concepts demonstrated
- Recursion with explicit base case
- Call stack depth = N (number of disks)
- Total moves = 2^N − 1

## RISC-V relevance
Each recursive call maps to a stack frame push on the CPU.
Relevant for understanding call overhead on embedded RISC-V boards.
