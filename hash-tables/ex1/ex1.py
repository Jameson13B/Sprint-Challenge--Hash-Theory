def get_indices_of_item_weights(weights, limit):
  dict = {}
  i = 0
  while i < len(weights):
    dict[weights[i]] = i
    i += 1
  for key in dict:
    try:
      difTest = dict[limit-key]
      if difTest:
        if dict[limit-key] > dict[key]:
          return (dict[limit-key], dict[key])
        else:
          return (dict[key], dict[limit-key])
    except KeyError:
        print('None: Next Key')
      

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  get_indices_of_item_weights([4, 6, 10, 15, 16], 21); 
  get_indices_of_item_weights([6, 8, 12, 17, 18], 30); 