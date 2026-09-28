import pathlib
import shutil
import sys
import time
from downloads_organizer_railerival import settings

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    print("\x1b[2J\x1b[H", end="")

def move(child_list) -> None:
    """moves the files and folders in their respective folder"""
    for (
        child
    ) in child_list:  # child = PosixPath('/home/rai/Desktop/fake_downloads/documents')
        for new_dir, extensions in settings.DIRECTORIES.items():
            new_dir_path = settings.DOWNLOADS_PATH / new_dir
            if isinstance(extensions, tuple) and bool(extensions):
                for extension in extensions:
                    if (child.suffix).lower() == extension and (not child.is_dir()):
                        move_command(child, new_dir_path)
            else:
                if not (child.suffix in settings.EXTENSION_LIST):
                    move_command(child, settings.MISCS_PATH)

def move_command(child, dst):
    """Moves child to dst, appending a counter if a file with the same name exists."""
    child_path = pathlib.Path(child)
    dst_dir = pathlib.Path(dst)

    target = dst_dir / child_path.name
    stem = child_path.stem
    suffix = child_path.suffix

    counter = 1
    while target.exists():
        target = dst_dir / f"{stem} ({counter}){suffix}"
        counter += 1

    shutil.move(child_path, target)

def update_child_list(child_list) -> None:
    """makes a list of childs of downloads folder excluding the custom directories"""
    for child in settings.DOWNLOADS_PATH.iterdir():
        if child not in settings.folder_path_list:
            child_list.append(child)

def make_dir() -> None:
    """makes dir from DIRECTORIES"""
    for new_dir, _ in settings.DIRECTORIES.items():
        new_dir_path = settings.DOWNLOADS_PATH / new_dir
        new_dir_path.mkdir(exist_ok=True)

def startswith_dot(string: str) -> bool:
    """checks if string startswitch dot and returns bool"""
    return string.startswith(".")


def main() -> None:
    """main function"""
    child_list = []
    ext_check = True

    clear_screen()
    time.sleep(2)
    for letter in "WELCOME TO DOWNLOADS_ORGANIZER!":
        print(letter, end="", flush=True)
        time.sleep(0.1)
    print()

    if settings.DOWNLOADS_PATH.is_dir():
        print("CHECK [✅]:the DOWNLOADS_DIR is a folder")
    else:
        print("CHECK [❌]:the DOWNLOADS_DIR is not a folder")
        sys.exit()

    for _, tuple_ in settings.DIRECTORIES.items():
        for element in tuple_:
            ext_check = startswith_dot(element) and ext_check

    if ext_check:
        print('CHECK [✅]:all the prefixes in DIRECTORIES starts with "."')
    else:
        print('CHECK [❌]:all the prefixes in DIRECTORIES doesn\'t start with "."')
        sys.exit()

    ext_check = True

    for string in settings.EXTENSION_LIST:
        ext_check = startswith_dot(string) and ext_check

    if ext_check:
        print('CHECK [✅]:all the prefixes in EXTENSION_LIST starts with "."')
    else:
        print('CHECK [❌]:all the prefixes in EXTENSION_LIST doesn\'t start with "."')

    update_child_list(child_list)

    make_dir()

    move(child_list)

    for letter in "PROGRAM EXECUTED!":
        print(letter, end="", flush=True)
        time.sleep(0.1)


if __name__ == "__main__":
    from cli import app
    app()