# code được tham khảo từ: https://www.youtube.com/watch?v=WViyCAa6yLI (time: 2:54:57)
from settings import * 
from os import walk
from os.path import join

def import_image(*path, alpha = True, format = 'png'):
	'''
	impoort hinh anh tu duong dan path
	'''
	full_path = join(*path) + f'.{format}'
	return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()

def import_folder(*path):
	'''
	import cac hinh anh tu folder path
	'''
	frames = []
	for folder_path, subfolders, image_names in walk(join(*path)):
		for image_name in sorted(image_names, key = lambda name: int(name.split('.')[0])):
			full_path = join(folder_path, image_name)
			frames.append(pygame.image.load(full_path).convert_alpha())
	return frames 

def import_folder_dict(*path):
	'''
	import cac hinh anh tu folder path va tra ve dictionary
	'''
	frame_dict = {}
	for folder_path, _, image_names in walk(join(*path)):
		for image_name in image_names:
			full_path = join(folder_path, image_name)
			surface = pygame.image.load(full_path).convert_alpha()
			frame_dict[image_name.split('.')[0]] = surface
	return frame_dict

def import_sub_folders(*path):
	'''
	import cac hinh anh tu cac sub folder cua path (trong folder path co nhieu sub folder chua cac hinh anh khac nhau)
	'''
	frame_dict = {}
	for _, sub_folders, __ in walk(join(*path)): 
		if sub_folders:
			for sub_folder in sub_folders:
				frame_dict[sub_folder] = import_folder(*path, sub_folder)
	return frame_dict
