# vim: set comments=sb\:\*,sb\:\ \ \ \*,mb\:\ \ \ -,ex-3\:\*,\:>,fb\:\*,fb\:-,\:»,fb\:»:
# vim: set fo=tcqrowpn:
# vim: set tw=120:

# Merge Intervals

## Overview
The **merge intervals** pattern deals with problems involving overlapping intervals. Each interval is represented by a 
start and end time. For example, an interval of [10,20] seconds means that the interval starts at 10 seconds and ends 
at 20 seconds, such that both 10 and 20 are included in the interval.

The most common problems solved using this pattern are scheduling problems.

The key to understanding this pattern and exploiting its power lies in understanding how any two intervals may 
overlap. The illustration below shows the six different ways in which two intervals can relate to each other:
	1. Intervals 1 and 2 don't overlap. Interval 1 ends before the start of Interval2:
	   |------Interval 1-------|
	                            |----Interval 2-----|
	2. Intervals 1 and 2 overlap. Interval 2 ends after Interval 1:
	   |------Interval 1-------|
	                      |-----Inverval 2-----|
	3. Interval 2 completely overlaps Interval 1:
	      |---Interval 1----|
	   |------Interval 2-------|
	4. Interval 1 and Interval 2 overlap. Interval 1 ends after Interval 2:
	       |------Interval 1-------|
	   |-----Interval 2-----|
	5. Interval 1 completely overlaps Interval 2:
	   |------Interval 1------|
	     |----Interval 2----|
	6. Interval 1 and 2 don't overlap. Interval 1 starts after the end of Interval 2:
	                       |-----Interval 1-----|
	   |----Interval 2----|

## Examples
The following examples illustrate some problems that can be solved with the merged intervals approach:

### Merge Overlapping Intervals
Intervals = [1,5],[4,6],[7,9],[8,9],[9,10]
<----1----2----3----4----5----6----7----8----9----10---->
    1|-------------------|5                  
                   4|---------|6             
                                  7|---------|9
                                       8|----|9
                                            9|----|10
List of Merged Intervals: [1,6],[7,10]

### Meeting Rooms
Given an array of meeting time intervals, determine if a person could attend all meetings.

#### Example 1
Intervals = [0,30],[5,10],[15,20]
<-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-> 
 0|-----------------------------------------------------------|30
           5|---------|10     15|---------|20
                     \overlapping/
Result = False
	Two intervals overlap with the first interval, hence te person cannot attend all the meetings.

#### Example 2
Intervals = [1,3],[10,15]
<-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0->   
   1|---|3          10|---------|15
Result = True
	The two intervals don't overlap, hence the person can attend both meetings.

## Does the Problem Match this Pattern?
* Yes, if both these conditions are fulfilled:
   * The input data is an array of intervals.
   * The problem requires dealing with overlapping intervals, either to find their intersection, their union, or the 
     gaps between them. This may be required as the final goal, or as an intermediate step in the computation of 
     intervals.
* No, if either of these conditions is fulfilled:
   * The order of the intervals in the result is not significant.
   * The input list of intervals is not sorted. In such a situation, we would prefer to use some other technique to 
     efficiently solve the problem.

## Real-World Problems
Many problems in the real world use the merge intervals pattern. The following are some examples:
* **Display Busy Schedule**: Display the busy hours of a user to other users without revealing the individual meeting 
  slots in a calendar
* **Schedule a New Meeting**: Add a new meeting to the tentative meeting schedule of a user in such a way that no two 
  meetings overlap each other.
* **Task Scheduling In Operating Systems (OS)**: Schedule tasks for the OS based on task priority and the free slots in 
   the machine's processing schedule.

## Match the Strategy Approach
1. Find the 4th largest element in an array: Some other Pattern
2. Schedule 3 interviews for an interviewer in on day: Merge Intervals
3. Find the intersection of two intervals: Merge Intervals
4. Find the 3rd closest point to the origin: Some other Pattern
