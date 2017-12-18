sample_input = "3, 4, 1, 5"
def figure_the_thing(input, length):
  input_list = [x for x in range(0, length)]
  index = 0
  skip_size = 0
  for item in input.split(', '):
    item_val = int(item)
    sub = []
    if index + item_val > len(input_list):
      sub = input_list[index:item_val-len(input_list)]
      sub = sub + input_list[0:(item_val-len(input_list))]
      index = item_val-len(input_list)
    else:
      sub = input_list[index:item_val]
      index += item_val
    skip_size += 1
    print(index)
    print(sub)
  return input_list  
new_list = figure_the_thing(sample_input, 5)
print(new_list[0]*new_list[1])

