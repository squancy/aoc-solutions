from collections import defaultdict
import re

ing = []
ALL_INGREDIENTS = []
ALL_ALLERGENS = []
for line in open('inp21.txt').readlines():
  line = line.rstrip()
  p = re.compile('(.+) \(contains (.+)\)') 
  obj = p.fullmatch(line)
  keys = obj.group(2).split(', ')
  v = obj.group(1).split(' ')
  ing.append([keys, v])
  ALL_INGREDIENTS.extend(v)
  ALL_ALLERGENS.extend(keys)

ALL_INGREDIENTS = set(ALL_INGREDIENTS)
ALL_ALLERGENS = set(ALL_ALLERGENS)

def can_contain_X(ingredient, allergen, ing):
  cont = True
  for pair in ing:
    if allergen in pair[0] and not ingredient in pair[1]:
      return False
  return cont

def count_occurrences(res, ing):
  cnt = 0
  for pair in ing:
    for r in res:
      cnt += pair[1].count(r)
  return cnt

def first_part(ing):
  res = set()
  for ingredient in ALL_INGREDIENTS:
    flag = True
    for allergen in ALL_ALLERGENS:
      if can_contain_X(ingredient, allergen, ing):
        flag = False
        break
    if flag:
      res.add(ingredient)
  
  return [count_occurrences(res, ing), res]

def clear_ingredients(ing, bad):
  new_ing = []
  for pair in ing:
    new_ing.append([pair[0], [x for x in pair[1] if not x in bad]])
  return new_ing

def sure(pres):
  for k, v in pres.items():
    if len(v) == 1:
      return k, v[0]

def remove_sure(pres, r):
  new_pres = {}
  for k, v in pres.items():
    new_pres[k] = [x for x in v if x != r] 
  return new_pres

def second_part(ing, bad, ALL_INGREDIENTS, ALL_ALLERGENS):
  ing = clear_ingredients(ing, bad) 
  ALL_INGREDIENTS -= bad
  pres = defaultdict(list)
  for ingredient in ALL_INGREDIENTS:
    for allergen in ALL_ALLERGENS:
      if can_contain_X(ingredient, allergen, ing):
        pres[ingredient].append(allergen) 

  res = {}
  for i in range(len(pres)):
    k, v = sure(pres)
    res[k] = v
    del pres[k]
    pres = remove_sure(pres, v)

  return ','.join({k: v for k, v in sorted(res.items(), key=lambda item: item[1])}.keys())

ans, res = first_part(ing)
print('First part:', ans)
print('Second part:', second_part(ing, res, ALL_INGREDIENTS, ALL_ALLERGENS))
