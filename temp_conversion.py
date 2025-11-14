# Todo: Code is a bit unclear

def Fc(x):
    Y = (x - 32) * (5 / 9)
    return Y

def FK(x):
    y = Fc(x)
    z = y + 273.15
    return z

def differencest(temp_list):
	differences = []
	for i in range(len(temp_list)):
		if i>0 and i<len(temp_list):
			differences.append(temp_list[i]-temp_list[i-1])
			print(f'Difference is {temp_list[i]-temp_list[i-1]}')
		else:
			pass
	return differences
	
