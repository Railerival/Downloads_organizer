import sys
import time
import shutil
import settings

child_list = []

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    print("\x1b[2J\x1b[H", end="")

def move(child_list) -> None:
    """moves the files and folders in their respective folder"""
    for child in child_list: # child = PosixPath('/home/rai/Desktop/fake_downloads/documents')
        for new_dir, extensions in settings.DIRECTORIES.items():
            new_dir_path = settings.DOWNLOADS_PATH / new_dir
            if isinstance(extensions, tuple) and bool(extensions):
                for extension in extensions:
                    if child.suffix == extension and (not child.is_dir()):
                        shutil.move(child, new_dir_path)
            else:
                if not(child.suffix in settings.EXTENSION_LIST):
                    shutil.move(child, settings.MISCS_PATH) 

def update_child_list(child_list) -> None:
    """makes a list of childs of downloads folder excluding the custom directories"""
    for child in settings.DOWNLOADS_PATH.iterdir():
        if child not in settings.folder_path_list:
            child_list.append(child)

def make_dir() -> None:
    """makes dir from DIRECTORIES"""
    for new_dir, _ in settings.DIRECTORIES.items():
        new_dir_path = settings.DOWNLOADS_PATH / new_dir
        new_dir_path.mkdir(exist_ok = True)
            
def main(child_list) -> None:
    """main function"""

    clear_screen()
    time.sleep(2)
    for letter in "WELCOME TO DOWNLOADS_ORGANIZER!":
        print(letter, end="" ,flush = True)
        time.sleep(0.1)
    print()

    if settings.DOWNLOADS_PATH.is_dir():
        print("CHECK [✅]:the DOWNLOADS_DIR is a folder")
    else:
        print("CHECK [❌]:the DOWNLOADS_DIR is not a folder")
        sys.exit()

    update_child_list(child_list)

    make_dir()
    
    move(child_list)
    for letter in "PROGRAM EXECUTED!":
            print(letter, end="" ,flush = True)
            time.sleep(0.1)

if __name__ == "__main__":
    main(child_list)
