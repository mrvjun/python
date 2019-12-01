#  @title：字符串
#  @name: MX
#  @return：null
#  @date：20191103

# 字符标题title()
numbers = ['one','Two','three']
print(numbers)
for num_0 in numbers:
		print(num_0.title() + ', how are you?')
print('\n')

# 字符大写upper()
for num_1 in numbers:
		print(num_1.upper() + ', how are you?')
print('\n')

# 字符小写lower()
for num_2 in numbers:
		print(num_2.lower() + ', how are you?')
print('\n')

# 字符去空格strip()
worlds = [' eight ', 'nine ', ' ten']
print(worlds)
for wor_0 in worlds:
		print(wor_0.strip() + ', how are you?')
print('\n')

# 字符去右空格rstrip()
for wor_1 in worlds:
		print(wor_1.rstrip() + ', how are you?')
print('\n')

# 字符去左空格lstrip()
for wor_2 in worlds:
		print(wor_2.lstrip() + ', how are you?')
print('\n')
