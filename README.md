## About

Advent of Code 2025 puzzles and (attempted) solutions. From: https://adventofcode.com/2025

I've always tried Advent of Code, but could never get past the first couple of days because the difficulty inevitably ramps up.

Rather than shamefully retreat into hibernation, I'd like to give each problem the good old college try. And if I haven't found a good solution by 6pm, I'd look one up.

Here are some day to day reflections as I complete / attempt the challenges.

## Daily Reflections

### Day 1

For the most part, I had a good idea of how to brute force my way through both parts. And those solutions are definitely brute forced.

For the most part, since I decided to do these in Python (second only to JavaScript/TypeScript), I spent a lot of time looking up the Python syntax for stuff like how to read files (for parsing the input), rounding (`math.floor` and `math.ceil`), and string and array methods.

### Day 2 & Day 3

The second part for each of these were really tough for me.

It's always such a plot twist when a solution works for the example input, but not the problem input.

For Day 2, I felt like I was very close to getting the solution in the second part, but I couldn't quite code it correctly. I had a real "aha" moment after looking up a solution.

For Day 3, I couldn't do the second part at all. I looked up some solutions and I couldn't understand many of them. I read something about "monotonic stack" and even watched some visualizations. But I still struggled with trying to code it.

### Day 4

After Day 3's failure, I decided to watch a [video about a monotonic stack](https://www.youtube.com/watch?v=cTBiBSnjO3c). TIL and it took a few times to watch, and ultimately I still didn't know how to apply it to that problem.

For the record, a monotonic stack is a stack whose elements are in either increasing or decreasing order.

But as I was reading the problem for Day 4, I decided to try something different. As soon as I saw the grid "blueprint", I had to hold back the internal dread long enough to watch a video about grids.

I watched another [NeetCode video](https://www.youtube.com/watch?v=pV2kpPD66nE), which was very helpful. The biggest takeaway was taking a step back to visualize the problem and solve it by hand.

[Manually solving the example input](./images/aoc2025_day4.png)

The Breadth-First Search algorithm was also useful. I've heard of it before, but wasn't comfortable implementing it. With some peeking, I was able to apply it to both parts and only had to introduce a couple different trackers in part 2.

I'm very proud of this one!