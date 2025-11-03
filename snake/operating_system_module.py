import os

cwd = os.getcwd()

print(cwd)
#/Users/shallow/Desktop/snake

folder_name = 'folder'
folder_path = r'/Users/shallow/Desktop'

def main():
    print("hello_world\n")
    if not os.path.exists(os.path.join(folder_path, folder_name)):
        os.makedirs(folder_name)
    

if __name__ == "__main__":
    main()




