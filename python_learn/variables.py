#  @title：变量和简单数据类型
#  @name：MX
#  @return：null
#  @date：20191103

# 创建整数列表range()
for num_1 in range(2,4):
	print(num_1)
print('\n')

# 创建列表list()
number_1 = list(range(5,25,3))
print(number_1)
print(min(number_1))
print(max(number_1))
print(sum(number_1))

num_1 = [num_1**2 for num_1 in number_1]
print(num_1)
print('\n')

# 从末尾开始定位
number_2 = list(range(0,19,3))
print('This is my teating:')
for num_2 in number_2[:-3]:
	print(str(num_2))
print('\n')

# 判断if elif else
number_3 = ['one','two','three','four']
for num_3 in number_3:
	if num_3 == 'two':
		print(num_3.upper())
	else :
		print(num_3.title())

num_a = 23
if num_a != 23:
	print('That is right!')
else:
	print('That is error!')
print('\n')

# 判断两个列表
number_all = list(range(-5,45,3))
number_4 = list(range(1,30,4))
print('This is number_all: ' + str(number_all))
print('This is number_4: ' + str(number_4))
for num_4 in number_4:
	if num_4 in number_all:
		print(str(num_4) + ' ' + 'It is right!')
	else:
		print(str(num_4) + ' ' + 'It is error!')
print('\n')
