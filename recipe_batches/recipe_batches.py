#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    obj = {}

    for key, value in ingredients.items():
        obj[key] = 0
        while value >= recipe[key]:
            obj[key] += 1
            value -= recipe[key]
        if len(ingredients) < len(recipe):
            return 0
        else:
            return min(obj.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))