#  @title：函数
#  @name: MX
#  @return：null
#  @date：20191110

# 函数def、返回值
def greet_user(uname, uage):
	print('Hello, ' +  uname.title() + ' is ' + uage + ' old.')
	allu = uname + ' ' + uage
	
	return allu.title() 
	
greet_user('xv', '21')
greet_user('vv', '22')

allus = greet_user('xj', '23')
print(allus)

# 传递列表
