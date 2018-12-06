# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator
global x
x=0
def main():
#    if (x==0):
 #       n = int(input("Please enter a whole number: "))
  #  else:
   #     n=x
    n=3
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)
    return fact
main()
