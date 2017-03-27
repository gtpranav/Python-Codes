import os
def rename_files(): 
    #get file list from folder
    file_list =  os.listdir(r"C:\Users\Pranav\Downloads\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Pranav\Downloads\prank\prank")
    #for each file, rename filename
    for file_name in file_list:
        print("old_name"+file_name)
        print("new_name"+file_name.translate(None , "0123456789"))
        os.rename(file_name , file_name.translate(None , "0123456789"))
        os.chdir(saved_path)
rename_files()
