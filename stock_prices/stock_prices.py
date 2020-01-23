#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # set the max profit
    max_profit_so_far = prices[1] - prices[0]
    # loop through and look for the smallest number from 1 to end indices
    for i in range(len(prices) - 1):
        # set the current_buy_price and find max_selling_price
        current_buy_price = prices[i]
        max_selling_price = max(prices[i + 1:])
        # calculate difference of buy and sell
        profit_potential = max_selling_price - current_buy_price
        # set value if found higher profit price
        if profit_potential > max_profit_so_far:
            max_profit_so_far = profit_potential
        # then return max_profit_so_far
    return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))