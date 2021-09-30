import pyautogui as auto
from PIL import Image
import random
import time
import aircv as ac
import numpy as np
import cv2
import keyboard
import sys
import threading
import os

class YYS():

	status = 'NORMAL'


	def __init__(self):
		self.screen_size = [x//2 for x in auto.size()]
		self.exit_thread = None

	
	def exitListener(self):
		def loopfunction():
			print('[INFO]---守护线程开启')
			keyboard.wait('f8')
			self.status = 'STOP'
			print('[INFO]---守护线程结束，此次结束后停止')
			# sys.exit(0)
			os._exit(0)
		thread = threading.Thread(target=loopfunction)
		thread.start()
		return thread

	'''
		找寻目标并且点击

		@parma picture_path 目标图片路径
		@parma pos_dim 模糊点击范围
		@parma time_dim 点击时间延迟随机数
		@parma accuracy 目标识别的准确率阈值
		@parma needMouseMove 寻找目标期间 是否模拟鼠标随机运动
	'''
	def clickTarget(self,picture_path,pos_dim=25,time_dim=4,accuracy=0.58,needMouseMove=False):

		target_picture = ac.imread(picture_path)
		isFound = False
		while isFound == False:
			screenshot = np.array(auto.screenshot())
			pos = ac.find_template(screenshot, target_picture)
			if pos and pos['confidence'] >= accuracy:
				pos_center = pos['result']
				tar_x = pos_center[0] + random.randint(-pos_dim,pos_dim)
				tar_y = pos_center[1] + random.randint(-pos_dim,pos_dim)
				time.sleep(random.uniform(time_dim/2,time_dim))
				auto.click((tar_x,tar_y))
				time.sleep(random.uniform(0,time_dim/2))
				auto.click((tar_x,tar_y))
				print('get found picture position at',pos_center)
				print(pos)
				ifFound = True
				break
			else:
				print('not found')
				if needMouseMove:
					self.mouseRandomMove()

	'''
		模拟鼠标随机运动或者点击

		@parma offset 以屏幕中心为起点，范围偏移量进行随机移动
		@parma time_dim 移动所需时间
		@parma click_th 每次移动有概率进行点击操作 默认25%
	'''
	def mouseRandomMove(self,offset = (200,50),time_dim = 2,click_th = 25):

		# 中下
		# x = self.screen_size[0] + random.randint(-offset[0],offset[0])
		# y = self.screen_size[1] + 200 + random.randint(-offset[1],offset[1])
		# 中上
		x = self.screen_size[0] + random.randint(-offset[0],offset[0])
		y = self.screen_size[1] - 300 + random.randint(-offset[1],offset[1])
		auto.moveTo(x,y,duration=random.uniform(0,time_dim))
		random_count = random.randint(0,500)
		if random_count < click_th:
			auto.click()
	
	'''
		测试用 寻找图片并且标记所在位置
	'''
	def drawPictureWhenFound(self,tar_picture,src_picture=None):
		def draw_circle(img, pos, circle_radius, color, line_width):
			cv2.circle(img, pos, circle_radius, color, line_width)
			cv2.imshow('objDetect', imsrc) 
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		if src_picture:
			imsrc = ac.imread('bg.jpg')
		else:

			imsrc = np.array(auto.screenshot())
		imobj = ac.imread(tar_picture)

		pos = ac.find_template(imsrc, imobj)
		if pos is None:
			print('Not Found')
			return
		circle_center_pos = pos['result']
		circle_radius = 50
		color = (0, 255, 0)
		line_width = 10

		print(pos['result'])
		print(pos)
		x,y=pos['result']

		m=int(x)
		n=int(y)
		circle_center_pos = pos['result']
		circle_radius = 50
		color = (0, 255, 0)
		line_width = 10

		draw_circle(imsrc, (m,n), circle_radius, color, line_width)

	def script(self):
		self.clickTarget('./picture/033.png')
		print('over 1')
		self.clickTarget('./picture/05.png',needMouseMove=True)
		print('over2')

	def run(self):
		self.exit_thread = self.exitListener()
		self.status = 'RUNING'
		while self.status == 'RUNING':
			try:
				self.script()
			except Exception as e:
				print('[ERROR]---发生错误，强制退出')
				print(e)
				self.status = 'ERROR'
				os._exit(0)

if __name__ == '__main__':
	yys = YYS()
	yys.run()
	# yys.drawPictureWhenFound('./picture/04.png')



	

	