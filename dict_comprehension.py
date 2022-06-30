def dict_comp(stop, step):

  list_items = []
  n = 1 
  for i in range(n,stop+1):
    arr =[] 
    for x in range(n,stop+1):
      if len(arr) < step:
        arr.append(x)
        if len(arr) == step:
          n = arr[-1]+1
          list_items.append(arr)
  
  items_dict ={f"item-{i+1}":x for i,x in enumerate(list_items)}
  return items_dict
print(dict_comp(20,4))