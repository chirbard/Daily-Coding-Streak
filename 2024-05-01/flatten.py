# define flatten() below...
def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print('List Found!')
      flat_list = flatten(item)
      for subitem in flat_list:
        result.append(subitem)
      continue
    result.append(item)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))