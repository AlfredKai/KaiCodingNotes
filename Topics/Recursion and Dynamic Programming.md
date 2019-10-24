# Recursion and Dynamic Programming

## Recursion

>Tip: In my experience coaching candidates, people typically have about 50% accuracy in their "this sounds like a recursive problem" instinct. Use that instinct, since that 50% is valuable. But don't be afraid to look at the problem in a different way, even if you initially thought it seemed recursive. There's also a 50% chance that you were wrong.

- Bottom-Up Approach: The key here is to think about how you can build the solution for one case off of the previous case (or multiple previous cases).
- Top-Down Approach: In these problems, we think about how we can divide the problem for case N into subproblems.
- Half-and-Half Approach - In addition to top-down and bottom-up approaches, it's often effective to divide the data set in half. For example, binary search and merge sort.

## Recursive vs.lterative Solutions

Recursive algorithms can be very space inefficient. Each recursive call adds a new layer to the stack, which means that if your algorithm recurses to a depth of n, it uses at least 0 (n) memory.

For this reason, it's often better to implement a recursive algorithm iteratively. *All* recursive algorithms can be implemented iteratively, although sometimes the code to do so is much more complex. Before diving into recursive code, ask yourself how hard it would be to implement it iteratively, and discuss the tradeoffs with your interviewer.

>Drawing the recursive calls as a tree is a great way to figure out the runtime of a recursive algorithm.

## Dynamic Programming & Memoization

Dynamic programming is mostly just a matter of taking a recursive algorithm and finding the overlapping subproblems (that is, the repeated calls). You then cache those results for future recursive calls.

Alternatively, you can study the pattern of the recursive calls and implement something iterative. You still "cache" previous work.

## Top-Down Dynamic Programming (or Memoization)

## Bottom-Up Dynamic Programming