# Recurrence-Relations
Date: April 20, 2021

Implement a function called **evaluaterecurrence** that takes as input a vector of integers
nvec and returns the total cost of evaluating a divide-and-conquer algorithm by evaluating
some recurrence relation for each value of n in nvec. Using function pointers/handles.

## Main Program
Write a main program that specifies an array of values of n in nvec and uses your function(s) to evaluate and plot the cost trends as a function of n for the following
recurrence relations:

1. T1(n) = 1 + 2T(n/2) + n (Merge Sort)
2. T2(n) = 2T(n − 1) + 1 (Tower of Hanoi)
3. T3(n) = 5T(n/3) + n
4. Factorial

## Data Collection and Analysis

The general trends for each recurrence relations is shown in the graphs below.

<img width="560" alt="Screen Shot 2021-06-03 at 3 19 15 PM" src="https://user-images.githubusercontent.com/73355680/120706716-09d86780-c47f-11eb-958b-b64200d3b753.png">


## Discussion 
1. Have you gained any intuition in analyzing recurrences from this exercise? That is, from the 4 recurrences given, can you summarize how features of the equation affect the change in asymptotic growth?

- I have gained intuition in analyzing recurrences from this exercise. We can see that if the equation is only be modify by a constant number then the growth will be slower, while if the equation has to operate by n factor (e.g with factorial problem) the growth will change really fast. Besides, if the equation modified by n/2, n/3 or a small sub number of n then the rate of growth is also slow.

2. What base cases did you implement for each of the recurrences and why? For one of the recurrences try changing the base case. Does it change the overall trend? Why or why not?

- Merge sort: n<2 (i.e n=0 or n=1) because in merge sort T(0) = T(1) = 0. This happens when the array/list has only 1 or 0 elements so nothing need to be done.
- Tower of Hanoi: n<1 this happens when there is only 1 disc, hence no moving around will be needed.
- T3(n): n<3 because we need the term n/3 to be larger or equal to 1, at n<3 then n/3 will a number smaller than 1.
- Factorial: n<1 because “the base case returns a value without making any subsequent recursive calls”3 and the smallest factorial we can have is 0!, no smaller sub problem can be broken to after that.

- When we change the base case, it does change the overall trend. This can be seen from practical test case. When I changed the base case of merge sort form n<2 to n<4 and n<6. As we know, in recursive the base case is like the foundation of a house, when we change it, it will eventually effect everything that built upon the base case. 

<img width="501" alt="Screen Shot 2021-06-03 at 3 23 06 PM" src="https://user-images.githubusercontent.com/73355680/120707127-92ef9e80-c47f-11eb-926e-19c929722c88.png">
