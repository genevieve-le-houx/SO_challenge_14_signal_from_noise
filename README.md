# Stackoverflow Challenge #14: Signal from Noise

This is my submission to Stackoverflow challenge #14: Signal from Noise

https://stackoverflow.com/beta/challenges/79838396/challenge-14-signal-from-noise

The goal is to find a continuous range from two integer, with exactly one integer missing and exactly one integer appears twice. 

The array may contain noise. The noise could form a mini sequence, but it will be shorter than the main sequence. 

The goal is to find the start value, end value, missing value and duplicate value.

The data is in the file ``number_sequences.txt``

It is also asked to compute the sum of the sequence start and end values. 

# Approach
My approach is simple. For each signal, the number are sorted. Then, I iterate over them and check if they form a sequence, if it is a duplicate value or a missing value. 
I also keep track of the sequence length to make sure it is the longest in the signal. 

# Execution

The code is done using Python 3.13.7. To execute, simply run ``main.py``. No library needed. 