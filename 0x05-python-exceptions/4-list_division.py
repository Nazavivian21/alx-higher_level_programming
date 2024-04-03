#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	new_list = []
	try:
		for i in range(list_length):
			result = my_list_1[i] / my_list_2[i]
			if not (isinstance(my_list_1[i], (int, float)) or isinstance(my_list_2[i], (int, float))):
				print("wrong type")
			new_list.append(result)
		return (new_list)
			# print (new_list)
	except TypeError:
		print("wrong type")
	except ZeroDivisionError:
		result = 0
		new_list.append(result)
		print("division by 0")

