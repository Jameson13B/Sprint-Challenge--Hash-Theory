def reconstruct_trip(tickets):
  # Create dict/hash table
  dict = {}
  rv = []
  for ticket in tickets:
    dict[ticket[0]] = ticket[1]

  try:
    # Set current and add to rv list
    current = dict[None]
    rv.append(current)
    next = dict[None]
    # Loop through until next is None
    while next != None:
      try:
        next = dict[next]
        if next:
          rv.append(next)
      except:
        return []
    return rv
  except:
    return 
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
