#  @title：字典
#  @name：MX
#  @return：null
#  @date：20191103

# 字典键值的增加、删除、更改
colours = {'world': 'red', 'x_num': 6, 'y_num': 7}
print(colours['world'])
print(colours['x_num'])
print(colours['y_num'])
print(colours)
print('\n')

# 字典键值的增加
colours['colour'] = 'green'
print(colours)
print('\n')

# 字典键值的更改
colours['colour'] = 'yellow'
colours['x_num'] = 4
print(colours)
print('\n')

# 字典键值的删除
del colours['world']
print(colours)
print('\n')

# 字典键值的增加、删除、更改
if colours['colour'] == 'blub':
	x_new_num = 1
elif colours['colour'] == 'green':
	x_new_num = 2
else:
	x_new_num = 3
colours['x_num'] = colours['x_num'] + x_new_num
print('x_new_num:' + ' ' + str(colours['x_num']))
print('\n')

# 字典键值的遍历
user_0 = {
	'xu': '123',
	'guan': '511',
	'luo': '145',
	'chen': '498',
	'zeng': '123',
	'li': '511'
	}
for uname_0, key in user_0.items():
	print('uname: ' + uname_0)
	print('key: ' + key + '\n')
print('\n')

# 字典键的遍历keys()
for uname_1 in user_0.keys():
	print(uname_1.title())
print('\n')

# 字典键的按序遍历sorted()	
for uname_2 in sorted(user_0.keys()):
	print(uname_2.title() + ', What is your key?' + '\n')
print('\n')

# 字典值的按序遍历values()	
for uname_3 in sorted(user_0.values()):
	print(uname_3.title() + ', That is cool!' + '\n')
print('\n')

# 字典值的集合遍历set()	
for uname_4 in set(user_0.values()):
	print(uname_4.title() + ', This is all number.' + '\n')
print('\n')

# 在列表中存储字典
aliens = []
for alien_num in range(10):
	new_alien = {'colour': 'yellow', 'points': '2', 'speed': 'slow'}
	aliens.append(new_alien)
print(aliens)

for alien in aliens[0:3]:
	if alien['points'] == '2':
		alien['colour'] = 'blue'
		alien['speed'] = 'fast'
		alien['points'] = '5'

for alien in aliens[0:5]:
	print(alien)
print('\n')

# 在字典中存储列表
pizzas = {}
pizzas['sweet'] = ['much', 'kiss', 'moon']
pizzas['salt'] = ['less', 'briny', 'sun']
pizzas['light'] = ['weak', 'wish', 'star']
pizzas['hot'] = ['spicy', 'acrid', 'earth']
print(pizzas)
for taste, toppings in pizzas.items():
	print('\n' + 'Toppings of ' + taste.title() + 'are: ')
	for topping in toppings:
		print(topping.title())
print('\n')

# 在字典中存储字典
users = {}
users['alibaba'] = {'uname': 'tbh', 'ukey': '455', 'uaddress': 'ua_0'}
users['tencent'] = {'uname': 'aws', 'ukey': '889', 'uaddress': 'ua_1'}
users['netaese'] = {'uname': 'mrh', 'ukey': '123', 'uaddress': 'ua_2'}
print(users)
print('\n')
for user_name, uaccounts in users.items():
	print('NET: ' + user_name)
	print('	account is: ' + str(uaccounts))
	print('		username is: ' + uaccounts['uname'])
	print('		userkey is: ' + uaccounts['ukey'])
	print('		useraddress is: ' + uaccounts['uaddress'])
	print('\n')
print('\n')
