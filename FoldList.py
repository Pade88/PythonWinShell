import os


#lv_FolderName = input("Insert New Folder name:")
#os.system('if not exist "C:\\Users\\ovidi\\Desktop\\{}" mkdir C:\\Users\\ovidi\\Desktop\\{}'.format(lv_FolderName, lv_FolderName))
#os.system('cd {}'.format(lv_FolderName))
#lv_FolderName2 = input("You've changed path, insert a new folder")
#os.system('mkdir C:\\Users\\ovidi\\Desktop\\{}\\{}'.format(lv_FolderName, lv_FolderName2))

print("------------------")
print("1. Show the files in the current directory")
print("2. Show current directory path")
print("3. Create a directory")
print("4. Rename a directory")
print("5. Delete a directory")
print("6. Navigate")
print("------------------")
while True:
	lv_switch_key = int(input())

	if lv_switch_key == 1:
		os.system('dir')
	if lv_switch_key == 2:
		lv_currentDirectory = os.getcwd()
		print(lv_currentDirectory)
	if lv_switch_key == 3:
		lv_FolderName = input("Insert folder name: ")
		os.mkdir(lv_FolderName)
	if lv_switch_key == 4:
		lv_OldName = input("Insert folder old name: ")
		lv_NewName = input("Insert folder new name: ")
		os.rename(lv_OldName, lv_NewName)
	if lv_switch_key == 5:
		lv_DeleteFolder = input("Insert folder to be deleted: ")
		os.rmdir(lv_DeleteFolder)
	if lv_switch_key == 6:
		lv_currentDirectory = os.getcwd()
		lv_cdLocation = input("CD: ")
		os.system('cd {}\\{}'.format(lv_currentDirectory, lv_cdLocation))
	if lv_switch_key == 0:
		break