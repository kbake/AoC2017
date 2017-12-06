test_input_str = "0	2	7	0"
test_input_str = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
test_input_list = [int(x) for x in test_input_str.split('\t')]
# Part 1
found_combos = []
cur_state = str.join(',', [str(x) for x in test_input_list])
tot = 0
while cur_state not in found_combos:
	found_combos.append(cur_state)
	#print(cur_state)
	biggest = test_input_list[0]
	biggest_index = 0
	counter = 0
	for val in test_input_list:
		if val > biggest:
			biggest = val
			biggest_index = counter
		counter += 1
	test_input_list[biggest_index] = 0
	cur_iter = biggest_index 
	for i in range(1, biggest+1):
		cur_iter += 1
		if cur_iter > len(test_input_list) - 1:
			cur_iter = 0
		test_input_list[cur_iter] += 1
	cur_state = str.join(',', [str(x) for x in test_input_list])
	tot += 1
print(tot)

# Part 2
tot = 0
to_search = cur_state
while True: 
	biggest = test_input_list[0]
	biggest_index = 0
	counter = 0
	for val in test_input_list:
		if val > biggest:
			biggest = val
			biggest_index = counter
		counter += 1
	test_input_list[biggest_index] = 0
	cur_iter = biggest_index 
	for i in range(1, biggest+1):
		cur_iter += 1
		if cur_iter > len(test_input_list) - 1:
			cur_iter = 0
		test_input_list[cur_iter] += 1
	cur_state = str.join(',', [str(x) for x in test_input_list])
	tot += 1
	if cur_state == to_search:
		break
print(tot)
