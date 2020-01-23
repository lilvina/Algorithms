#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={0: 0, 1: 1, 2: 2}):
    # make a counter to count how many cookies are eaten
    # make a recursive function 
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        my_cookies = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        cache[n] = my_cookies
        return my_cookies


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')