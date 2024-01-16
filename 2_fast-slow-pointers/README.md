# vim: set comments=s6b\:\ \ \ \*,mb\:\ \ \ \ \ \ -\,ex-3\:\ \ \ \*,\:>,fb\:\*,fb\:-:
# vim: set fo=tcq1rowpn:
# vim: set tw=0:

# Fast and Slow Pointers
## Introduction
Fast and slow pointers approaches are usually used to identify distinguishable features of directional data structures, such as linked list or an array.

The pointers can be used to traverse the array or list in either direction, however, *one moves faster than the other*. Generally, the slow pointer moves forward by a *factor of one*, and the fast pointer moves by a *factor of two* in each step. However, the ***speed can be adjusted according to the problem statement***.

Unlike the two pointer approach, which is concerned with data values, the fast and slow pointers approach is used to **determine data structure traits** using indicies in arrays or node pointers in linked lists. The approach is commonly used to **detect cycles** in the given data structure, so it's also known as ***Floyd's cycle detection*** algorithm.

The key idea is:
* The pointers start at the same location and move at different speeds.
* **If there is a cycle**, then the two are bound to meet at some point in the traversal.

**To understand the concept**:
Imagine two runners on a track. While they start from the same point, they have different running speeds. If the race track is a circle, the faster runner will overtake the slower one after completing a lap. On the other hand, if the track is straight, the faster runner will end the race before the slower one, hence never meeting on the track again. The fast and slow pointers pattern uses the same intuition.

#### Example
Take the following array or linked list:
```
SF
2->4->6->8->10`
       ↖ <- ↲
```
* The slow and fast pointers initially point to the first index(node) in the array list. 
* Increment the **slow** pointer by 1 and the **fast** pointer by 2.
* The redirection of arrows represents a cycle in the list.

In the array list above, the iteration eventually reaches the point where *slow* points to 6 and fast points to 10. Then in the next iteration both slow and fast pointers will meet, pointing at the index/node with value 8. Thus, indicating a cycle.

#### Example Problems
* Find the middle node in a linked list
Set the **fast** and **slow** pointers initially equal to the head of the linked list. Traverse the linked list by moving the **slow** pointer one node forward, and the **fast** pointer two nodes forward. Once the **fast** pointer reaches the last node, the **slow** pointer hsa reached the middle node of the linked list.
```
                   F          F
HEAD -> 7 -> 10 -> 3 -> 15 -> 24 -> NULL
```

* Determine if an integer is a happy number
A step represents calculating the sum of the squares of the individual digits of the integer. The **slow** pointer moves one step, and the **fast** pointer moves two steps. This process is repeated until either the **fast** pointer becomes equal to **1**, in which case the initial integer is a *happy number*. Otherwise, if the **fast** and **slow** pointers meet, *a cycle exists* in the pattern of numbers, so the initial integer is **not** a happy number.
```
            S            F
19 -> 82 -> 68 -> 100 -> 1
```
In the example above, the **fast** pointer eventually becomes equal to **1**, so **19** is a **happy number**.

## Does the problem match this pattern?
* **Yes**, if either of these conditions is fulfilled:
   - Either as an intermediate step, or as the final solution, the problem requires identifying:
   	- the first *x*% of the elements in a linked list, or,
   	- the element at the *k-way* point in a linked list, for example, the middle element, or the element at the start of the second quartile, etc...
	- the *k^th^* last element in a linked list
   - Solving the problem requires detecting the presence of a cycle in a linked list.
   - Solving the problem requires detecting the presence of a cycle in a sequence of symbols.
* **No**, if either of these conditions is fulfilled:
   - The input data cannot be traversed in a linear fashion, that is, it's neither in an array nor in a linked list, nor in a string of characters.
   - The problem can be solved with two pointers traversing an array or linked list at the same pace.

## Real-World Problems
* **Symlink verification**: Fast and slow pointers can be used in a symlink verification utility in an operating system. A symbolic link, or symlink, is simply a shortcut to another file. Essentially, it's a file that points to another file. Symlinks can easily create loops or cycles where shortcuts point to each other. To avoid such occurrences, a symlink verification utility can be used.
  Similar to linked lists, fast and slow pointers can detect a loop in the symlinks by moving along the connected filies or directories at different speeds.
* **Compiling an object-oriented program**: Usually programs are not contained in a single file. Particularly, for large applications, modules can be divided into different files for better maintenance. Dependency relationships are then defined to specify the order of compilation in these files. However, sometimes, there might be cyclic dependencies that can lead to an error.
  Fast and slow pointers can be used to identify and remove these cycles for seamless compilation and execution of the program.
