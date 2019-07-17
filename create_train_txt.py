import os
'''
	这是一个yolov3的工具，它可以实现将所有jpg文件路径整合到一个train.txt文件中，你可以自己设置图像的路径以及输出的txt文件的路径。
'''

img_path = '/media/ljq/文档/刘佳奇/深度学习之Tensorflow工程化项目实战/第8章_卷积神经网络(CNN)——在图像处理中应用最广泛的模型/实例44用YOLO3模型识别门牌号/8-13  yolov3numbers/data/img'
txt_path = '/home/ljq/桌面/未命名文件夹/'

with open(txt_path + 'train.txt','w') as f:
	for root,dir_path,filename in os.walk(img_path):
		for i in range(len(filename)):
			file_path = root + '/' + filename[i]
			f.write(file_path+'\n')
		


