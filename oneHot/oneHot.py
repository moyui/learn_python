import pickle

container = {}
text = ''

def wrapOperate(container, text, num = 0):

	def operate(container, count , item):#隐含的计数器
		if not(item in container):
			container[item] = count
			count += 1

		return container, count


	def readFiles(container, text):
		with open('./实验1data.txt', 'r') as f:
			count = num
			for line in f.readlines():
				text += line
				line = line.strip('\n')
				tempArr = line.split(' ')
				for item in tempArr:
					(container, count) = operate(container, count, item)

		return container, text


	(fs, text) = readFiles(container, text)

	return fs, text

(container, text) = wrapOperate(container, text)

#存取
g = open('dump.txt', 'wb')
pickle.dump(container, g)
g.close()

#读出
h = open('dump.txt', 'rb')
y = pickle.load(h)
h.close()

#翻译
text = text.replace('\n', '')
fin = text.split(' ')
for i in range(len(fin)):
	if fin[i] in y:
		fin[i] = y[fin[i]]

print(fin)