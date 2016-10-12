"""In pseudocode, this looks like the following. At the top level, we'll call MoveTower with disk=5, source=A, dest=B, and spare=C.

FUNCTION MoveTower(disk, source, dest, spare):
IF disk == 0, THEN:
    move disk from source to dest
ELSE:
    MoveTower(disk - 1, source, spare, dest)   // Step 1 above
    move disk from source to dest              // Step 2 above
    MoveTower(disk - 1, spare, dest, source)   // Step 3 above"""


"""A key to solving this puzzle is to recognize that it can be
solved by breaking the problem down into a collection of smaller
problems and further breaking those problems down into even
smaller problems until a solution is reached. For example:

label the pegs A, B, C
let n be the total number of discs
number the discs from 1 (smallest, topmost) to n (largest, bottommost)
To move n discs from peg A to peg C:

move n−1 discs from A to B. This leaves disc n alone on peg A
move disc n from A to C
move n−1 discs from B to C so they sit on disc n

The above is a recursive algorithm, to carry out steps 1 and 3, apply
the same algorithm again for n−1. The entire procedure is a finite
number of steps, since at some point the algorithm will be required
for n = 1. This step, moving a single disc from peg A to peg C, is
trivial. This approach can be given a rigorous mathematical formalism
with the theory of dynamic programming,[7][8] and is often used as an
example of recursion when teaching programming."""