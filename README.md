# How to run
### Default : ./sorting_deck.py N1, N2, N3, ... (bubble sort)
### Choice algorihm : /sorting_deck.py --algo [bubble/insert/quick/merge]  N1, N2, N3, ... 
### GUI option : /sorting_deck.py N1, N2, N3, ... --gui 

When given a series of numbers as input, your program will sort them using the algorithm specified on the command line. It will output the different steps of the sorting operation on stdout, or display them in the GUI if the GUI option is specified.

In the core part of the project, you will implement the following algorithms:

    bubble sort
    insertion sort
    quick-sort
    merge sort

Because understanding algorithms and their complexity is essential to become a well-rounded engineer (... you will also need it to pass technical interviews!), you also need to research the complexity of those algorithms. During the code review, you must be able to describe the worst/average/best cases of those algorithms.

Note: Obviously you won't get any skill points if you don't understand perfectly what you have implemented.
Directions

Your program must be called sorting_deck.py and be present at the root of your git repository.

The arguments to the --algo option are bubble, insert, quick and merge. If the option --algo is not specified, the default algorithm will be bubble sort.

A --gui option will display a graphical representation of the sort with the pyglet library that you know already. You must be able to display inputs of up to 15 integers in the core part of the project (you can handle larger inputs as a bonus). This limit is only for the GUI mode, the default mode should of course handle inputs of all sizes.

In non-GUI mode, the outputs on stdout will be as follow:

    Bubble sort: you will output the list after each swap of integers
    Insertion sort: you will output the list after each insertion operation placing a number at its right place in the sorted list
    Quick sort: you will output the pivot and the list after each partition operation (you can choose the pivot however you want)
    Merge sort: you will output the merged list after each merge of two sublists. The Sentinel will assume that you recursively sort the left half of a list first.

You have to respect those output directions strictly, otherwise the Sentinel won't be able to assess that you correctly implemented your algorithm.
The algorithm visualisator

The GUI must display the list of integers and the different changes leading to the list being sorted. You are free to represent the list the way you want, to have animations for moving around the integers, etc - be creative, as long as the different steps of the algorithm are perfectly understandable!

It will also showcase which element the algorithm is at, at any moment. For example the bubble sort will run over the whole list as long as it finds at least one element unsorted. This passing over the list must be visualised (for example, you can have each element highlighted as the algorithm loops over it).

Your GUI must have a step by step mode where hitting a keyboard key moves the algorithm to the next step.

All those elements will be checked manually during the review, as the Sentinel is GUI-blind!

Important note: all your code related to the GUI should be imported only if the --gui option is specified. First, to respect clean design principles (don't import useless modules!), and secondly because importing pyglet in the Sentinel will make it crash.
The Sentinel

The Sentinel will only review the algorithms on stdout.

However, don't forget to run the Sentinel at the end of your project, to check that you still pass pycodestyle (you should never push on your remote repository dirty code anyway!) and the basic tests. Don't allow regressions to ruin your early work!
