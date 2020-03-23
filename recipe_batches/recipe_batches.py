#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  num_of_batches = None
  current_batch = 0

  for k,v in recipe.items():
    
    if not k in ingredients:
      return 0
    current_batch = ingredients[k] // v
    if not num_of_batches and (current_batch >= 1):
      num_of_batches = current_batch
    print(current_batch)
    if 0 < current_batch < num_of_batches:
      num_of_batches = current_batch

  return num_of_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))