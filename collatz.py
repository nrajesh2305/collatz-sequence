# No imports are necessary for this file.

# Replace with the portfolio website when done.
website_url = ""

def printIntro():
    print("\nCollatz Sequence, or the 3n + 1 Problem\nBy Nithin Rajesh " + website_url + "\n\nThe Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:\n\n1) If n is even, the next number is n / 2.\n2) If n is odd, the next number n is n * 3 + 1.\n3) If n is 1, stop. Otherwise, repeat.\n\nIt is generally thought, but so far not mathematically proven, that every starting number eventually terminates at 1.\n")

def performFormula(number):
    fullSequence = ""
    while True:
        if(number == 1):
            fullSequence += str(1)
            break
        fullSequence += str(number) + " "
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    return fullSequence
