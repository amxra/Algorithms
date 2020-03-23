#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
   min_price = 0
   max_profit = None

  for i in range(len(prices) - 1):
    min_price = prices[i]
    for j in range(i, len(prices)):
      current_profit = prices[j] - min_price
      if not max_profit:
        max_profit = current_profit
      if current_profit > max_profit:
        max_profit = current_profit

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))