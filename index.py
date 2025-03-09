import os
import shutil
import tkinter as tk
from tkinter import filedialog
import sys

folder_path = " "
new_folder_path = " "
new_folder_name = " "
file_path = " "
file_type = " "
#opens and selects folder
def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()
    return folder_path

print("This program will open up your window explorer and allow you to pick a folder that has the files that you want to move. \n\n"  
      "It will allow you to create an new folder or an existing folder. \n\n"
      "Then you will choose which file type to move to the new or exising folder. \n\n"
      "All files with that type (ex. txt, py, etc) will be moved to new folder location.\n\n"
      "At any point in time, type 'quit!' to end the program.")

#checks if quit! is inputed and ends the program
def check_for_quit(input):
    if input.lower() == "quit!":
        print("Program ended.")
        sys.exit(0)
    
#check if folder was selected or not and assigns path as string to folder_path
if __name__ == "__main__":
    selected_folder = select_folder()
    if selected_folder:
        folder_path = selected_folder       
        while True:
            create_new_folder = input("Would you like to: (1) create a new folder or (2) move to an existing one: ") 
            check_for_quit(create_new_folder)  
            #will loop until a 1 or 2 is entered.
            if create_new_folder == "1":
                check_for_quit(create_new_folder) 
                #creates new folder with new name in parent of the original folder               
                new_folder_name = input("Please enter new folder name: ")  
                check_for_quit(new_folder_name)                           
                os.makedirs(os.path.dirname(folder_path) + "/" + new_folder_name)
                new_folder_path = str(os.path.dirname(folder_path) + "/" + new_folder_name)
                break               
            elif create_new_folder == "2":
                check_for_quit(create_new_folder)
                new_folder_path = input("Please paste folder path: ")
                check_for_quit(new_folder_path)                 
                break
            else:
                print("Please enter '1' or '2'")
                check_for_quit(create_new_folder) 
    else:
        print("No folder selected. Program ended.")
        os._exit(0)      
    
#checks if extension type matches any files in folder
def extension_checker(file_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(file_extension):
            return True

#if valid file type exists, then continue with the program    
while True:
    file_type = input("Please enter the file type you want moved: ") 
    check_for_quit(file_type)   
    if extension_checker(file_type) == True:
        print("Valid file type") 
        break
    else:
        print("No file type exists in this folder. Please type again: ")

def delete_folder_contents(old_folder_path):
    for filename in os.listdir(old_folder_path):
        file_path = os.path.join(old_folder_path, filename)
        print(file_path)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                #if valid file, move to new folder, then delete in the old folder
                if file_type in file_path:
                    shutil.move(file_path, new_folder_path)
                    print(f"File '{file_path}' moved successfully to '{new_folder_path}'")   
                                              
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

delete_folder_contents(folder_path)
