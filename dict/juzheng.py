in1 = [[1, 2, 7], [2, 1, 18], [2, 1, 5]]
in2 = [[1, 2, 6], [3, 4, 7]]
out = []

def judgeMuti(in1, in2):
	if (len(in1) == len(in2[0])):
		return '可以相乘'
	else:
		return '不能相乘'

def muti(in1, in2, out):

	flag = judgeMuti(in1, in2)
	print(flag)
	if (flag == '不能相乘'):
		return

	tempIn1 = list(zip(*in1))

	for j in range(len(in2)):
		tempList = []

		for i in range(len(tempIn1)):
			tempList.append(sum(list(map(lambda a, b: a*b, tempIn1[i], in2[j]))))

		out.append(tempList)

	return out

print(muti(in1, in2 ,out))
