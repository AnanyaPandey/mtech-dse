1. Machine A runs a program in 100 seconds, Machine B runs the same program in 125 seconds. How much faster is Machine A than B?
    
   Performance A / Performance B = 125/100 = 1.25
   therefore A = 1.25 times faster than B

2. Computer A has 2 GHz clock. It takes 10s CPU time to finish one given task. We want to design Computer B to finish the same task within 5s CPU time. The clock cycle number for computer B is 2 times as that of Computer A. What clock rate should be designed for Computer B?

Clock rate A = 2 x 10^9 clock cycles / sec
Clock rate B = ?
Execution time in A = 10s
Execution time in A = 5s

N = number of clock cycles reqiured for the program
N for A = 10 * 2 * 10^9 => 2 * 10^10
N for B = 2 * 2 * 10^ 10 => 4 * 10^10 
N for B = 40 * 10^9

Therefore now since it takes 5s 
Clock rate B = 40 * 10^9 / 5 = 8 * 10^9 or 8 Ghz

3. If 70% of a program is speeded up by making it execute on 8 CPU’s parallelly. What is the maximum speedup we can expect?

Overall speedup as per amdahl's law : (1/(1-p))
1/0.3 = 3.34 times.

4. Suppose we have two implementations of the same instruction set architecture (ISA). For some program, Machine A has a clock cycle time of 10 ns and a CPI of 2.0. Machine B has a clock cycle time of 20 ns and a CPI of 1.2. Which machine is faster for this program, and by how much?

1 clock cycle time of A = 10ns.
1 clock cyclt time of B = 20ns.

Average Clocks / Instructions (A) = 2.0 
Average Clocks / Instructions (B) = 1.2

Let there be number of instructions = I 

number of clock cycles (A) = 2I 
number of clock cycles (B) = 1.2I

Execution time for A = 10ns * 2I 
Exuction time for B = 20ns * 1.2I 

PerformanceA /Performance B = ExeutiontimeB/Executiontime A = 24/20 = 1.2 
Therefore A is 1.2 times faster than B.  