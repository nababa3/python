# initialize the first two Fibonacci numbers
fib1 = 0
fib2 = 1
# initialize the sum variable to zero
sum_fib = 0
# loop over the first 50 Fibonacci numbers
for i in range(50):
# add the current Fibonacci number to the sum
sum_fib += fib1
# calculate the next Fibonacci number
fib_next = fib1 + fib2
# update the values of fib1 and fib2 for the next iteration
fib1 = fib2
fib2 = fib_next
# print the sum of the first 50 Fibonacci numbers
print("The sum of the first 50 Fibonacci numbers is:", sum_fib)