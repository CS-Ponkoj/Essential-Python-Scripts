# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:15:13 2021

@author: csponkoj
"""


import os

# function that returns size of a file
def get_file_size(path):

	# getting file size in bytes
	size = os.path.getsize(path)

	# returning the size of the file
	return size


# function to delete a file
def remove_file(path):

	# deleting the file
	if not os.remove(path):

		# success
		print(f"{path} is deleted successfully")

	else:

		# error
		print(f"Unable to delete the {path}")


def main():
	# specify the path
	path = "ENTER_PATH_HERE"

	# put max size of file in MBs
	size = 500

	# checking whether the path exists or not
	if os.path.exists(path):

		# converting size to bytes
		size = size * 1024 * 1024

		# traversing through the subfolders
		for root_folder, folders, files in os.walk(path):

			# iterating over the files list
			for file in files:
				
				# getting file path
				file_path = os.path.join(root_folder, file)

				# checking the file size
				if get_file_size(file_path) >= size:
					# invoking the remove_file function
					remove_file(file_path)
			
		else:

			# checking only if the path is file
			if os.path.isfile(path):
				# path is not a dir
				# checking the file directly
				if get_file_size(path) >= size:
					# invoking the remove_file function
					remove_file(path)


	else:

		# path doesn't exist
		print(f"{path} doesn't exist")

if __name__ == '__main__':
	main()