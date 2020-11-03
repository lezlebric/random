# 產生一個1~100隨機數
# 用家不斷估
# 估錯要提用家仲差幾多

import random

r = random.randint(1, 100)
while True:
	num = input('請輸入一個數字: ')
	num = int(num)
	if num == r:
		print('你估中咗!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')


