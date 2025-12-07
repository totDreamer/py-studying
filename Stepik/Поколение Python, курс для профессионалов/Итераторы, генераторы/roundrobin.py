def roundrobin(*args):
  iter_list =[iter(arg) for arg in args]
  queue = []
  while iter_list != []:
    for it in iter_list:
      try:
        yield next(it)
        queue.append(it)
      except:
        continue
    iter_list, queue = queue[:], []