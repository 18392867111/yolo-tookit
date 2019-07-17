import xml.dom.minidom
import os

'''
	这是一个标注风格转化的工具，可以将PascalVOC风格的xml文件，转化为<x_center>,<y_center>,<width>,<height>类型的.txt的文件。
	它包含了两个函数：
		read_xml_dir(dir_path)
		write_yolo3_txt(xlm_filename,txt_output_path)
	其中，
		read_xml_dir(dir_path)
			功能： 输入xml文件地址，输出一个包含文件夹下所有xml文件名称的列表。

		write_yolo3_txt(xlm_filename,txt_output_path)
			功能：输入xml文件名称的列表以及想要输出的txt文件地址，实现txt文件的输出(与xml文件名称保持一致)，无return。
'''

def read_xml_dir(dir_path):
	xlm_filenames = []
	for root,dir_path,filename in os.walk(xml_input_path):
		for i in range(len(filename)):
			xlm_filenames.append(root + filename[i])
	return xlm_filenames

def write_yolo3_txt(xlm_filename,txt_output_path):
	dom = xml.dom.minidom.parse(xlm_filename)
	root = dom.documentElement
	xml_boxlabel_numeric = root.getElementsByTagName('name')
	xml_box_xmin = root.getElementsByTagName('xmin')
	xml_box_ymin = root.getElementsByTagName('ymin')
	xml_box_xmax = root.getElementsByTagName('xmax')
	xml_box_ymax = root.getElementsByTagName('ymax')
	xml_img_width = root.getElementsByTagName('width')[0].firstChild.data
	xml_img_height = root.getElementsByTagName('height')[0].firstChild.data
	txt_filename = xlm_filename.split('/')[-1][0:5]+'.txt'
	with open(txt_output_path + txt_filename,'w') as f:
		for i in range(len(xml_boxlabel_numeric)):
			xml_box_x_center = round((int(xml_box_xmin[i].firstChild.data)+(int(xml_box_xmax[i].firstChild.data)-int(xml_box_xmin[i].firstChild.data))/2)/int(xml_img_width),2)
			xml_box_y_center = round((int(xml_box_ymin[i].firstChild.data)+(int(xml_box_ymax[i].firstChild.data)-int(xml_box_ymin[i].firstChild.data))/2)/int(xml_img_height),2)
			xml_box_width = round((int(xml_box_xmax[i].firstChild.data)-int(xml_box_xmin[i].firstChild.data))/int(xml_img_width),2)
			xml_box_height = round((int(xml_box_ymax[i].firstChild.data)-int(xml_box_ymin[i].firstChild.data))/int(xml_img_height),2)
			f.write(dic[xml_boxlabel_numeric[i].firstChild.data]+' '+str(xml_box_x_center)+' '+str(xml_box_y_center)+' '+str(xml_box_width)+' '+str(xml_box_height)+'\n')

if __name__ == '__main__':
	dic = {'y':'0','n':'1'}
	xml_input_path = '/home/ljq/桌面/未命名文件夹/xml/'
	xlm_filenames = read_xml_dir(xml_input_path)
	txt_output_path = '/home/ljq/桌面/未命名文件夹/yolo3_txt/'

	for xlm_filename in xlm_filenames:	
		write_yolo3_txt(xlm_filename,txt_output_path)


