

"""
A happy number is defined by following:
Starting with any positive integer, replace the number with sum of it's digits,
repeat the process until the number either equals to 1 or it loops in a cycle
which does not include 1.

Those with number 1 are called happy numbers and others are unhappies. :)
"""



def counter(r , s):
    i = 0
    while i != r:
        print(str(s) + " is " + str(happy_checker(s)))
        s += 1
        i += 1
        

def happy_checker(n):
    nums = set()
    h = "Happy!"
    uh = "Unhappy."
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in nums:
            return uh
        nums.add(n)
    return h

def main():
    ask = input("specific number or a list?(s/l)")
    if ask == "s":
        number = int(input("Enter Number:"))
        print(happy_checker(number))
    elif ask == "l":
        rounds = int(input("how many numbers to check?"))
        start = int(input("where to start?"))
        counter(rounds , start)
    else:
        print("invalid input(either s for specific and l for list is accpeted)")

main()
