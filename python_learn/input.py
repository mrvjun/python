#  @title：输入和while循环
#  @name: MX
#  @return：null
#  @date：20191103

# 输入函数input()
messages = 'Please enter a number.'
messages += '\nWhat is your age? '
ages = input(messages)
ages = int(ages)
if ages % 2 == 0:
	print(str(ages) + ', ' + 'This number is even.')
else:
	print(str(ages) + ', ' + 'This number is odd.')
	
if ages >= 21:
	print('You are a adult.')
elif ages < 0:
	print('It is a error number.')
else:
	print('You are a child.')

# 循环while(break、continue)
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	if message == 'cmd':
		break
	if message == 'cool':
		continue
	else:
		print(message)
print('\n')

#用while循环来处理列表和字典
uc_users = ['acd', 'bre', 'can']
c_users = []
while uc_users:
	c_user = uc_users.pop()
	print('Verifying: ' + c_user.title())
	c_users.append(c_user)
print('\nThe following users have been confirmed:')
for c_user in c_users:
	print(c_user.title())

responses = {}
polling_active = True
while polling_active:
	name = input('\nWhat is your name?')
	response = input('Which mountain would you like to climb someday?')
	responses[name] = response
	repeat = input('Would you like to let another person respond? (yes/no)')
	if repeat == 'no':
		polling_active = False
print('\n---Poll results---')
for name, response in responses.items():
	print(name + ', would like to climb' + response + '.')
