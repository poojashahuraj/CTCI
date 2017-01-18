# coding=utf-8
"""
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and
we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the
given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for
corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
"""

input_arr = [100, 80, 60, 70, 60, 75, 85]
def stock_span_problem(ip):
    op = [0]*len(ip)
    for i in range(len(ip)):
        for j in range(i, -1, -1):
            if ip[j] > ip[i]:
                break
            elif ip[j] <= ip[i]:
                op[i] += 1
    return op
# this is brute force approach with o(n^2) time complexity
print stock_span_problem(input_arr)


# A linear time solution for stack stock problem

# A stack based efficient method to calculate s
def calculateSpan(price, S):
    n = len(price)
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while (len(st) > 0 and price[st[0]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) <= 0 else (i - st[0])

        # Push this element to stack
        st.append(i)


# A utility function to print elements of array
def printArray(arr, n):
    for i in range(0, n):
        print arr[i],


# Driver program to test above function
price = input_arr
S = [0 for i in range(len(price) + 1)]

# Fill the span values in array S[]
calculateSpan(price, S)

# Print the calculated span values
printArray(S, len(price))

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
